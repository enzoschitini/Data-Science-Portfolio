
import pandas as pd

class GuidaDataframe:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def esplorazione(self):
        righe, qnt_colonne = self.data_frame.shape
        quantita_righe = format(righe, ",").replace(',', '.')
        sequenza = list(range(qnt_colonne + 1))
        sequenza = sequenza[1:]

        colonne = self.data_frame.columns.to_list()
        types_list = [str(type(self.data_frame[col][0])).split("'")[1] for col in self.data_frame.columns]
        lista_categorias = [self.data_frame[col].nunique() for col in self.data_frame.columns]

        elementos_nulos = self.data_frame.isnull().sum()
        elementos_nulos = elementos_nulos.to_list()

        memoria = (self.data_frame.memory_usage(deep=True) / (1024 ** 2)).round() # Mb
        lista_memoria = memoria.to_list()
        lista_memoria = lista_memoria[1:]

        memoria = self.data_frame.memory_usage(deep=True) # Total Mb
        memoria_total = round(memoria.sum() / (1024 ** 2), 2)

        percentagem_dados_nulos = round((self.data_frame.isnull().sum() / righe) * 100)
        percentagem_dados_nulos = percentagem_dados_nulos.to_list()

        dados = pd.DataFrame({'Nome': colonne, 
                             'Tipo': types_list, 
                             'qnt_categorias': lista_categorias,
                             'Dados nulos' : elementos_nulos,
                             'Dados nulos %' : percentagem_dados_nulos,
                             'Memória (Mb)': lista_memoria}, index=sequenza)
        
        # Títulos
        print('Tabela Exploratória')
        print(f'Nesses dados temos {quantita_righe} linhas e {qnt_colonne} colunas.')
        print(f'Consumo de memória: {memoria_total}Mb.')
        
        return dados
