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

    pl = Analise
    pl.painel_geral(df, 'Petróleo Brasileiro S.A. - Petrobras (PBR)', "img\Petrobras.png")

elif resposta == 'Coca-Cola':
    df = pd.read_csv('Data\The Coca-Cola Company (KO).csv')

    pl = Analise
    pl.painel_geral(df, 'The Coca-Cola Company (KO)', "img\Coca-Cola.png")

elif resposta == 'Amazon':
    df = pd.read_csv('Data\Amazon - Stock market shares.csv')

    pl = Analise
    pl.painel_geral(df, 'Amazon - Stock market shares', "img\Amazon.png")

elif resposta == 'Tesla':
    df = pd.read_csv('Data\Tesla, Inc. (TSLA).csv')

    pl = Analise
    pl.painel_geral(df, 'Tesla, Inc. (TSLA)', "img\Tesla.png")

elif resposta == 'Itaú Unibanco':
    df = pd.read_csv('Data\Itaú Unibanco Holding S.A. (ITUB).csv')

    pl = Analise
    pl.painel_geral(df, 'Itaú Unibanco Holding S.A. (ITUB)', "img\Itaú.png")

elif resposta == 'Emirates':
    df = pd.read_csv('Data\Emirates Global Sukuk S USD Acc.csv')

    pl = Analise
    pl.painel_geral(df, 'Emirates Global Sukuk S USD Acc', "img\Emirates.png")