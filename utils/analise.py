import streamlit as st
import yfinance as yf
import pandas as pd
from utils.graficos import FinancialPlots
import plotly.graph_objects as go
import itertools
import time

class Analise():
    def __init__(self):
        pass 

    def painel_geral(dataframe, nome, imagem):
        dataframe = pd.DataFrame(dataframe)
        col1, col2 = st.columns([3, 1])
        valor_minimo = 0
        valor_maximo = 3000
        fp = FinancialPlots()

        with col1:
            def status_da_acao(dataframe):
                # Supondo que você já tenha carregado os dados em um DataFrame chamado df

                # Ordenar os dados pela coluna 'Data' do mais antigo para o mais recente
                dataframe = dataframe.sort_values(by='Data')

                # Último dia de dados
                ultimo_dia = dataframe.iloc[-1]

                # Fechamento de hoje e de ontem
                fechamento_hoje = ultimo_dia['Fechamento']
                fechamento_ontem = dataframe.iloc[-2]['Fechamento'] if len(dataframe) > 1 else None

                # Verificar se a ação está crescendo
                if fechamento_ontem is not None:
                    if fechamento_hoje > fechamento_ontem:
                        return f'### A ação está crescendo'
                    elif fechamento_hoje < fechamento_ontem:
                        return f'### A ação está em queda'
                    else:
                        return f'### A ação manteve o mesmo valor de fechamento'
                else:
                    return f'### Não há dados suficientes para determinar o crescimento'

            # Ensure 'Data' column is in datetime format
            dataframe['Data'] = pd.to_datetime(dataframe['Data'])
            max_data = dataframe['Data'].max()
            min_data = dataframe['Data'].min()

            # Set minimum and maximum values for the slider
            #valor_minimo = dataframe['Value'].min()  # Assuming there's a 'Value' column
            #valor_maximo = dataframe['Value'].max()
                
            bar1, bar2 = st.columns([1, 1])

            with bar1:
                st.write(status_da_acao(dataframe))
                linhas, colunas = dataframe.shape
                #st.write(f'{linhas} registros analisados')
                valor_selecionado = st.slider("Escolha o valor", 7, 300, value=30)
                
            with bar2:
                data_inicial = st.date_input('Data inicial',
                            value=min_data,
                            min_value=min_data,
                            max_value=max_data)
                
                data_final = st.date_input('Data final',
                            value=max_data,
                            min_value=min_data,
                            max_value=max_data)
            
            # Convert date inputs back to datetime
            data_inicial = pd.to_datetime(data_inicial)
            data_final = pd.to_datetime(data_final)

            # Filter the dataframe based on the selected date range
            dataframe_filtered = dataframe[(dataframe['Data'] >= data_inicial) & (dataframe['Data'] <= data_final)]
            dataframe = dataframe_filtered
            
            st.write('#')
            st.write(f"### Índice {nome} nos últimos {valor_selecionado} dias")
            fp.Candlestick(valor_selecionado, dataframe, 'Ko') 
            st.write('### Distribuição dos preços de abertura, alta, baixa e fechamento')
            fp.int_boxplot(dataframe)

            with st.expander("Desempenho ao Longo do Tempo"):
                numeriocos = dataframe.drop(columns=['MA7', 'MA14', 'MA30'])
                numeriocos = numeriocos.select_dtypes('number').columns

                for x in numeriocos:
                    fp.line_gra(dataframe, x)

                fig = go.Figure()
                fig.add_trace(go.Scatter(x=dataframe['Data'], y=dataframe['MA7'], mode='lines', name='MA7'))
                fig.add_trace(go.Scatter(x=dataframe['Data'], y=dataframe['MA14'], mode='lines', name='MA14'))
                fig.add_trace(go.Scatter(x=dataframe['Data'], y=dataframe['MA30'], mode='lines', name='MA30'))
                fig.update_layout(title='Médias Móveis dos Preços de Fechamento')
                st.plotly_chart(fig, use_container_width=True)

            with st.expander("Scatter Plot (Gráficos de Dispersão)"):
                def mostrar_relacoes():
                    lista = ['Abertura', 'Alta', 'Baixa', 'Fechamento', 'Fechamento Ajustado',
                            'Volume', 'Amplitude', 'Porcentagem de crescimento anual',
                            'Porcentagem de crescimento diário', 'Crescimento Diário Absoluto']

                    pares = [list(par) for par in itertools.combinations(lista, 2)]

                    for x in pares:
                        fp.combinacoes(x, dataframe)
            
                def simulated_process():
                    for percent_complete in range(100):
                        time.sleep(0.1)
                        yield percent_complete + 1

                start_loading = st.button("Inicie o processo")

                if start_loading:
                    st.markdown(
                        """
                        <style>
                        .stProgress > div > div > div > div {
                            background-color: #FF7115;
                        }
                        </style>
                        """,
                        unsafe_allow_html=True
                    )
                    progress_bar = st.progress(0)

                    for percent_complete in simulated_process():
                        progress_bar.progress(percent_complete)
                    
                    mostrar_relacoes()
            
            with st.expander("Sobre os dados"):
                #st.image("img\pngamazon-logo-s3f.png", width=300)
                markdown_text = """
                ## Informações sobre as colunas
                1. **Data**: A data específica da entrada.
                2. **Abertura**: O preço da abertura do ativo no início do dia.
                3. **Alta**: O preço mais alto atingido pelo ativo durante o dia.
                4. **Baixa**: O preço mais baixo atingido pelo ativo durante o dia.
                5. **Fechamento**: O preço do ativo ao final do dia.
                6. **Fechamento Ajustado**: O preço de fechamento ajustado para dividendos e desdobramentos.
                7. **Volume**: O número de ações negociadas durante o dia.
                8. **Amplitude**: A diferença entre o preço mais alto e o mais baixo do dia (Alta - Baixa).
                9. **MA7**: Média móvel do preço de fechamento dos últimos 7 dias.
                10. **MA14**: Média móvel do preço de fechamento dos últimos 14 dias.
                11. **MA30**: Média móvel do preço de fechamento dos últimos 30 dias.
                12. **Retorno Diário**: A variação percentual do preço de fechamento em relação ao dia anterior.
                13. **TR (True Range)**: A maior diferença entre:
                    - O preço máximo do dia menos o preço mínimo do dia.
                    - O preço máximo do dia menos o preço de fechamento do dia anterior.
                    - O preço mínimo do dia menos o preço de fechamento do dia anterior.
                14. **ATR (Average True Range)**: Média móvel do True Range (TR) para um determinado período, usado para medir a volatilidade.
                15. **Dia**: O dia da semana.
                16. **Mês**: O mês do ano.
                17. **RSI (Relative Strength Index)**: Índice de Força Relativa, um indicador de momento que mede a velocidade e a mudança dos movimentos de preço.
                18. **Percentuale Crescita Annuale**: Percentual de crescimento anual.
                19. **Percentuale Crescita Giornaliera**: Percentual de crescimento diário.
                20. **Crescita Assoluta Giornaliera**: Crescimento absoluto diário, a diferença absoluta no preço de fechamento em relação ao dia anterior.

                Essas colunas fornecem uma visão detalhada sobre os preços e a performance de um ativo ao longo do tempo, incluindo indicadores de tendência e volatilidade.
                """
                st.write(f'## Dataset:')
                st.write(f'*{linhas} linhas e {colunas} colunas*')
                st.write(dataframe)
                st.markdown(markdown_text)

        with col2:
            def download_csv(dataframe, file_name):
                csv = dataframe.to_csv(index=False)
                csv = csv.encode('utf-8')
                st.download_button(label="📥 Bixar os dados das ações nesse período", data=csv, file_name=file_name, mime='text/csv')

            st.image(imagem)
            st.header(nome)
            st.write("Questo è il contenuto della seconda colonna, che è più piccola.")
            file_name = f"{nome}.csv"
            download_csv(dataframe, file_name)
            st.write('---')

            st.write('#### Médias da ação:')

            for x in numeriocos:
                col = dataframe[x].mean()
                st.write(f'##### Preço de {x}: --- **{round(col, 2)}**')
                #st.write(f'### {round(col, 2)}')