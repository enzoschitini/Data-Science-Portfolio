import streamlit as st
import pickle

st.set_page_config(
    page_title="My Streamlit App",  # Title of the app
    page_icon=":smiley:",           # Icon of the app
    layout="wide",                  # Layout of the app ('centered' or 'wide')
    initial_sidebar_state="expanded" # Sidebar state ('auto', 'expanded', 'collapsed')
)

with open('LGBMClassifier.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Nuovi dati per fare previsioni
new_data = [[5.1, 3.5, 1.4, 0.2],  # Aspetto di una Iris-setosa
            [6.7, 3.0, 5.2, 2.3]]  # Aspetto di una Iris-virginica

# Fare previsioni
#predictions = loaded_model.predict(new_data)

st.sidebar.write('Ok')
st.write('Ok')
