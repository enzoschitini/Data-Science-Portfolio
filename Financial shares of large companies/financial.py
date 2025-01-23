import streamlit as st
import pandas as pd
from pandas_datareader import data as web

from plotly.graph_objs import Layout
import plotly.graph_objects as go

from utils.pages import PagesLive
from utils.guida import GuidaDataframe
from utils.analise import Analise
from utils.graficos import FinancialPlots

st.set_page_config(layout='wide', page_title='Financial shares of large companies',
                   page_icon="img\Icone.png")
pl = PagesLive

st.sidebar.image("img\Investment 1.png")
st.sidebar.write('# Financial shares of large companies')
st.sidebar.write('Filtro do dataset - Escolha como quer ver os dados:')

resposta = st.sidebar.selectbox(f"Escolha uma empresa:", ['Petrobras', 'Coca-Cola', 'Amazon', 'Tesla', 'Itaú Unibanco', 'Emirates'])
st.write(f"Você escolheu:")
st.write(f'## {resposta}')

if resposta == 'Petrobras':
    df = pd.read_csv('Data\Petróleo Brasileiro S.A. - Petrobras (PBR).csv')
    #df = pl.dataframe_ativo('PBR', resposta)
    #df = pl.engenharia_de_atributos(df)

    pl = Analise
    pl.painel_geral(df, 'Petróleo Brasileiro S.A. - Petrobras (PBR)', "img\Petrobras.png")