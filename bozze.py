import streamlit as st
import pandas as pd
from pandas_datareader import data as web

from plotly.graph_objs import Layout
import plotly.graph_objects as go

import yfinance as yf

def dataframe_ativo(ativo, nome='Nome'):
    dt_ini, dt_fim = '2022-06-10', '2024-06-10'
    df = pd.DataFrame(yf.download(ativo, start=dt_ini, end=dt_fim))

    df['Amplitude'] = df['High'] - df['Low']
    df = df.reset_index()
    
    df.rename(columns={
        'Date': 'Data',
        'Open': 'Abertura',
        'High': 'Alta',
        'Low': 'Baixa',
        'Close': 'Fechamento',
        'Adj Close': 'Fechamento Ajustado',
        'Volume': 'Volume'
    }, inplace=True)

    #df.to_csv(f'{nome}.csv')
    return df

df = dataframe_ativo('KO', 'Coca-Cola (KO)')

from utils.guida import GuidaDataframe
Tabela_Exploratoria = GuidaDataframe(df).esplorazione()

st.write('# Financial shares of large companies')
st.write(df.head())
st.write(Tabela_Exploratoria)

from utils.pages import PagesLive
pl = PagesLive

# Variáveis
elemento_01 = 1
elemento_02 = 0

import streamlit as st

# Estado inicial dos elementos
if 'show_elemento_01' not in st.session_state:
    st.session_state.show_elemento_01 = False

if 'show_elemento_02' not in st.session_state:
    st.session_state.show_elemento_02 = False

# Função para alternar a visibilidade do elemento 01
def toggle_elemento_01():
    st.session_state.show_elemento_01 = not st.session_state.show_elemento_01

# Função para alternar a visibilidade do elemento 02
def toggle_elemento_02():
    st.session_state.show_elemento_02 = not st.session_state.show_elemento_02

# Botão para mostrar/ocultar o elemento 01
if st.button('Mostrar/Ocultar Elemento 01'):
    toggle_elemento_01()

# Botão para mostrar/ocultar o elemento 02
if st.button('Mostrar/Ocultar Elemento 02'):
    toggle_elemento_02()

# Verificação das variáveis e exibição do texto correspondente
if st.session_state.show_elemento_01:
    st.write("Este é o texto para o elemento 01, que aparece quando a variável elemento_01 é igual a 1.")
    
if st.session_state.show_elemento_02:
    st.write("Este é o texto para o elemento 02, que aparece quando a variável elemento_02 é igual a 1.")


import streamlit as st

# Imposta il titolo dell'applicazione
st.title('Esempio Interattivo di Cards con Pulsante Interno')

# Variabile per monitorare il clic
if 'card_clicked' not in st.session_state:
    st.session_state['card_clicked'] = ''

# Funzione per aggiornare lo stato della variabile
def update_card_click(card_name):
    st.session_state['card_clicked'] = card_name

# Crea una colonna per ogni card
col1, col2, col3 = st.columns(3)

# URL delle immagini (puoi sostituire con i tuoi URL)
cover_image_url = "https://via.placeholder.com/150"
profile_image_url = "https://via.placeholder.com/50"

# Card 1
with col1:
    st.markdown(f"""
    <div style="padding: 10px; border-radius: 5px; text-align: center;">
        <img src="{cover_image_url}" alt="Cover" style="width:100%; border-radius: 5px 5px 0 0;">
        <h3>Card 1</h3>
        <p>Questa è la descrizione della prima card. È possibile aggiungere più dettagli qui.</p>
        <div style="display: flex; align-items: center;">
            <img src="{profile_image_url}" alt="Profile" style="width: 40px; height: 40px; border-radius: 50%;">
            <span style="margin-left: 10px;">Nome Autore</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button('Clicca qui', key='1'):
        update_card_click('Card 1')

# Card 2
with col2:
    st.markdown(f"""
    <div style="padding: 10px; border-radius: 5px; text-align: center;">
        <img src="{cover_image_url}" alt="Cover" style="width:100%; border-radius: 5px 5px 0 0;">
        <h3>Card 2</h3>
        <p>Questa è la descrizione della seconda card. Puoi personalizzarla come preferisci.</p>
        <div style="display: flex; align-items: center;">
            <img src="{profile_image_url}" alt="Profile" style="width: 40px; height: 40px; border-radius: 50%;">
            <span style="margin-left: 10px;">Nome Autore</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button('Clicca qui', key='2'):
        update_card_click('Card 2')

# Card 3
with col3:
    st.markdown(f"""
    <div style="padding: 10px; border-radius: 5px; text-align: center;">
        <img src="{cover_image_url}" alt="Cover" style="width:100%; border-radius: 5px 5px 0 0;">
        <h3>Card 3</h3>
        <p>Questa è la descrizione della terza card. Aggiungi qualsiasi informazione tu voglia.</p>
        <div style="display: flex; align-items: center;">
            <img src="{profile_image_url}" alt="Profile" style="width: 40px; height: 40px; border-radius: 50%;">
            <span style="margin-left: 10px;">Nome Autore</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button('Clicca qui', key='3'):
        update_card_click('Card 3')

# Mostra il valore della variabile aggiornata
st.write(f"Hai cliccato su: {st.session_state['card_clicked']}")


st.write('In questo esempio, abbiamo una funzione simulated_process() che simula un processo che impiega del tempo.')



import streamlit as st
import time

# Funzione che simula un processo che impiega del tempo
def simulated_process():
    for percent_complete in range(100):
        time.sleep(0.1)  # Simula un processo che impiega del tempo
        yield percent_complete + 1

# Definire una variabile di controllo per avviare la barra di caricamento
start_loading = st.button("Avvia il processo")

# Avviare il processo solo se il pulsante viene premuto
if start_loading:
    # Iniettare il CSS per cambiare il colore della barra di progresso
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
    
    # Creare una barra di caricamento
    progress_bar = st.progress(0)
    
    # Eseguire il processo simulato
    for percent_complete in simulated_process():
        progress_bar.progress(percent_complete)
