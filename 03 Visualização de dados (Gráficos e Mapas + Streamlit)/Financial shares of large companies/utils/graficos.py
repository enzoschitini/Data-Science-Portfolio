from plotly.graph_objs import Layout
import plotly.graph_objects as go
import streamlit as st

class FinancialPlots():
    def __init__(self):
        pass 

    def nome(self, nome):
        print(nome)

    def Candlestick(self, total_de_registros, dataframe, nome):
        ATIVO = dataframe.tail(total_de_registros)

        graph = go.Candlestick(
            x=ATIVO.index,
            open=ATIVO['Abertura'],
            high=ATIVO['Alta'],
            low=ATIVO['Baixa'],
            close=ATIVO['Fechamento'],
            name='^BVSP'
        )

        layout = Layout(
            paper_bgcolor='white',
            plot_bgcolor='white',
            #title=f"Índice {nome} nos últimos {total_de_registros} dias",
            height=600,  # Defina a altura desejada
        )

        fig = go.Figure(
            data=[graph],
            layout=layout
        )

        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')

        # Adiciona CSS para definir a largura máxima
        max_width = 1000  # Defina a largura máxima desejada
        st.markdown(
            f"""
            <style>
            .reportview-container .main .block-container{{
                max-width: {max_width}px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        st.plotly_chart(fig, use_container_width=True)
    
    def grafico_de_pizza(lista1, lista2, lista3):
        fig = go.Figure(data = go.Pie(labels = lista1,
                                    values = lista2,
                                    marker_colors = lista3,
                                    hole = 0.5,
                                    pull = [0, 0, 0.15, 0, 0]))

        #Rótulos
        fig.update_traces(textposition = "outside", textinfo = "percent+label")

        #Legenda
        fig.update_layout(legend_title_text = "c",
                        legend = (dict(orientation = "h",
                                    xanchor = "auto",
                                    x = 0.5)))

        #Texto
        fig.update_layout(annotations = [dict(text = "c",
                                            x = 0.5,
                                            y = 0.5,
                                            font_size = 18,
                                            showarrow = False)])


        st.plotly_chart(fig, use_container_width=True)

    def line_gra(self, dataframe, coluna):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dataframe['Data'], y=dataframe[coluna], mode='lines', name=coluna, line=dict(color='#FF7115')))
        fig.update_layout(title=f'{coluna} ao Longo do Tempo')
        st.plotly_chart(fig, use_container_width=True)
    
    def int_boxplot(self, dataframe):
        fig = go.Figure()
        fig.add_trace(go.Box(y=dataframe['Abertura'], name='Abertura', marker=dict(color='#FF7115'), line=dict(color='#FF7115')))
        fig.add_trace(go.Box(y=dataframe['Alta'], name='Alta', marker=dict(color='#FF7115'), line=dict(color='#FF7115')))
        fig.add_trace(go.Box(y=dataframe['Baixa'], name='Baixa', marker=dict(color='#FF7115'), line=dict(color='#FF7115')))
        fig.add_trace(go.Box(y=dataframe['Fechamento'], name='Fechamento', marker=dict(color='#FF7115'), line=dict(color='#FF7115')))
        st.plotly_chart(fig, use_container_width=True)
    
    def combinacoes(self, lista:list, dataframe):
        r1 = lista[0]
        r2 = lista[1]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dataframe[r1], y=dataframe[r2], mode='markers', name=f'{r1} vs {r2}', marker=dict(color='#FF7115')))
        fig.update_layout(
            title=f'Relação entre {r1} & {r2}',
            xaxis_title=r1,
            yaxis_title=r2
        )
        st.plotly_chart(fig, use_container_width=True)