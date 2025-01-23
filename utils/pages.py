import streamlit as st
import yfinance as yf
import pandas as pd

class PagesLive():
    def __init__(self):
        pass 

    def dataframe_ativo(ativo, nome='Nome'):
        dt_ini, dt_fim = '2014-06-10', '2024-06-10'
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

    def engenharia_de_atributos(dataframe):
        df = dataframe

        df['MA7'] = df['Fechamento'].rolling(window=7).mean()
        df['MA14'] = df['Fechamento'].rolling(window=14).mean()
        df['MA30'] = df['Fechamento'].rolling(window=30).mean()

        df['Retorno Diário'] = df['Fechamento'].pct_change()

        df['True Range (TR)'] = df[['Alta', 'Baixa', 'Fechamento']].apply(lambda x: max(x['Alta'] - x['Baixa'], abs(x['Alta'] - x['Fechamento']), abs(x['Baixa'] - x['Fechamento'])), axis=1)
        df['Average True Range (ATR)'] = df['True Range (TR)'].rolling(window=14).mean()

        # Define the period for RSI calculation (typically 14 days) #######################################################
        period = 14

        # Calculate daily changes in closing prices
        df['Delta'] = df['Fechamento'].diff()

        # Separate gains (positive changes) and losses (negative changes)
        df['Gain'] = df['Delta'].apply(lambda x: x if x > 0 else 0)
        df['Loss'] = df['Delta'].apply(lambda x: -x if x < 0 else 0)

        # Calculate Average Gain and Average Loss over the specified period
        df['Average Gain'] = df['Gain'].rolling(window=period, min_periods=1).mean()
        df['Average Loss'] = df['Loss'].rolling(window=period, min_periods=1).mean()

        # Calculate RS (Relative Strength)
        df['Relative Strength (RS)'] = df['Average Gain'] / df['Average Loss']

        # Calculate RSI using the formula
        df['Relative Strength Index (RSI)'] = 100 - (100 / (1 + df['Relative Strength (RS)']))

        # Drop intermediate columns if needed
        df.drop(['Delta', 'Gain', 'Loss', 'Average Gain', 'Average Loss', 'Relative Strength (RS)'], axis=1, inplace=True)

        # Calculate daily returns ##########################################################################################
        df['Rendimento Diário'] = df['Fechamento'].pct_change() * 100

        # Calculate cumulative returns
        df['Retorno Cumulativo'] = (1 + df['Rendimento Diário'] / 100).cumprod() - 1

        # Calculate annualized growth percentage
        n_days = len(df)
        annual_growth_pct = ((1 + df['Retorno Cumulativo'].iloc[-1]) ** (365 / n_days) - 1) * 100

        # Append the annual growth percentage to each row (assuming it's the same for each day)
        df['Porcentagem de crescimento anual'] = annual_growth_pct

        # Drop intermediate columns if needed
        df.drop(['Rendimento Diário', 'Retorno Cumulativo'], axis=1, inplace=True)

        # ############################################

        df['Porcentagem de crescimento diário'] = df['Fechamento'].pct_change() * 100
        df['Crescimento Diário Absoluto'] = df['Fechamento'].diff()

        nome_dia = {
            "Monday": "Segunda-feira",
            "Tuesday": "Terça-feira",
            "Wednesday": "Quarta-feira",
            "Thursday": "Quinta-feira",
            "Friday": "Sexta-feira",
            "Saturday": "Sábado",
            "Sunday": "Domingo"
        }

        nome_mes = {
            "January": "Janeiro",
            "February": "Fevereiro",
            "March": "Março",
            "April": "Abril",
            "May": "Maio",
            "June": "Junho",
            "July": "Julho",
            "August": "Agosto",
            "September": "Setembro",
            "October": "Outubro",
            "November": "Novembro",
            "December": "Dezembro"
        }


        df['Dia'] = df['Data'].dt.day_name().replace(nome_dia)
        df['Mês'] = df['Data'].dt.month_name().replace(nome_mes)

        return df