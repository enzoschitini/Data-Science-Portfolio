import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('DataFrame_Crédito.csv').drop(columns='Unnamed: 0')
df['default_cat'] = df['default']
df['default_cat'] = df['default_cat'].astype('object')

st.write('# Credit Card Approval Prediction')
st.write('## Analytics Setup')

# Função para análise bivariada de variáveis numéricas
def AB2N(dataframe, x_coluna, y_coluna):
    tabela = dataframe.groupby(x_coluna)[y_coluna].mean().to_dict()
    fig = px.line(x=list(tabela.keys()), y=list(tabela.values()), 
                  title=f'Média de: {x_coluna} vs {y_coluna}', 
                  labels={'x': x_coluna, 'y': 'Média de ' + y_coluna})
    st.plotly_chart(fig)

# Função para análise bivariada entre variável categórica e numérica
def num_cat_analysis(dataframe, num_col, cat_col):
    fig = go.Figure()
    for cat in dataframe[cat_col].unique():
        filtered_data = dataframe[dataframe[cat_col] == cat][num_col]
        fig.add_trace(go.Box(
            y=filtered_data,
            name=cat,
            boxmean='sd',
            marker_color='rgba(255, 100, 102, 0.7)',
            line_color='rgba(255, 100, 102, 0.9)'
        ))
    fig.update_layout(
        title=f"Análise Bivariada: {num_col} por {cat_col}",
        xaxis_title=cat_col,
        yaxis_title=num_col,
        boxmode='group',
    )
    st.plotly_chart(fig)

# Função para análise bivariada entre variáveis categóricas
def AB2C(dataframe, col1, col2, metric):
    if metric == 'qtd':
        title = 'Análise Bivariada de Variáveis Categóricas'
        yaxis_title = 'Frequência'
        crosstab = pd.crosstab(dataframe[col1], dataframe[col2])
    elif metric == 'prct':
        title = 'Análise Bivariada de Variáveis Categóricas'
        yaxis_title = 'Percentual %'
        crosstab = pd.crosstab(dataframe[col1], dataframe[col2], normalize='index')

    color_palette = [
        'blue', 'orange', 'green', 'red', 'purple', 'cyan', 'magenta', 'yellow', 'brown', 'pink',
        'lime', 'indigo', 'teal', 'navy', 'gold', 'silver', 'gray', 'lightblue', 'darkgreen', 'lightcoral',
        'coral', 'lightgreen', 'darkviolet', 'crimson', 'salmon', 'khaki', 'plum', 'wheat', 'lavender',
        'peachpuff', 'lightpink', 'lightyellow', 'mediumseagreen'
    ]

    colors = {col: color for col, color in zip(crosstab.columns, color_palette[:len(crosstab.columns)])}
    
    fig = go.Figure()

    for col in crosstab.columns:
        fig.add_trace(go.Bar(
            name=col,
            x=crosstab.index,
            y=crosstab[col],
            marker_color=colors.get(col, 'gray')
        ))

    fig.update_layout(
        title=title,
        xaxis_title=col1,
        yaxis_title=yaxis_title,
        barmode='stack',
        legend_title=col2,
    )
    st.plotly_chart(fig)

def main():
    with st.expander("Ver dataframe"):
        st.write(df)
    
    with st.expander("### Análise bivariada de duas variáveis ​​numéricas"):
        x_coluna = st.selectbox('Selecione a coluna do eixo X', df.select_dtypes('number').columns, key='x_col_1')
        y_coluna = st.selectbox('Selecione a coluna do eixo Y', df.select_dtypes('number').columns, key='y_col_1')
        AB2N(df, x_coluna, y_coluna)

    with st.expander("### Análise bivariada entre uma variável categórica e outra numérica"):
        x_coluna = st.selectbox('Selecione a coluna do eixo X', df.select_dtypes('object').columns, key='x_col_2')
        y_coluna = st.selectbox('Selecione a coluna do eixo Y', df.select_dtypes('number').columns, key='y_col_2')
        num_cat_analysis(df, y_coluna, x_coluna)

    with st.expander("### Análise bivariada de duas variáveis ​​categóricas"):
        x_coluna = st.selectbox('Selecione a coluna do eixo X', df.select_dtypes('object').columns, key='x_col_3')
        y_coluna = st.selectbox('Selecione a coluna do eixo Y', df.select_dtypes('object').columns, key='y_col_3')
        AB2C(df, x_coluna, y_coluna, 'prct')
        AB2C(df, x_coluna, y_coluna, 'qtd')

if __name__ == "__main__":
    main()
