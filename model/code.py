import pandas as pd
import numpy as np

import lightgbm as lgb
from imblearn.over_sampling import SMOTE

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('DataFrame_Crédito.csv')

DF_ML = pd.get_dummies(df, drop_first=True)
"""
Transforma variáveis categóricas (como gênero ou estado civil) em variáveis numéricas, 
criando colunas binárias para cada categoria. 
Essa técnica é crucial para algoritmos de aprendizado de máquina que operam com dados numéricos.
"""

# Separação de Características e Variável Alvo:
y = DF_ML.default
X = DF_ML.drop(columns='default', axis=1)

# Divisão em Conjuntos de Treinamento e Teste:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)
"""
Divide os dados em dois conjuntos: treinamento (80%) e teste (20%). O conjunto de treinamento será usado para treinar o modelo, 
enquanto o conjunto de teste será usado para avaliar sua performance.
"""

# Padronização das Características:
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)                   
X_test = scaler.transform(X_test)
"""
Cria um objeto 'StandardScaler' para padronizar as características, o que significa que as coloca em uma 
mesma escala (média 0 e desvio padrão 1). Essa padronização é importante para evitar que características com escalas 
diferentes influenciem o modelo de forma desproporcional.
"""

# Pré-processamento de Dados e Balaceamento:
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
"""
O SMOTE é uma técnica de sobreamostragem que gera novos exemplos sintéticos da classe minoritária (provavelmente a classe 'default' neste caso, pois o default é um evento raro). 
Isso ajuda a reduzir o viés no conjunto de dados e a melhorar a performance do modelo.
"""

# Modelagem e Treinamento:
clf = lgb.LGBMClassifier(n_estimators=100, learning_rate=0.1,  # Seleção do Modelo
                        max_depth=3, random_state=42)
# Hiperparâmetros: Os hiperparâmetros (nestimators, learningrate, max_depth) influenciam a complexidade e o desempenho do modelo.

clf.fit(X_train_res, y_train_res) # Treina o modelo usando os dados de treinamento balanceados.

# Previsões sobre os dados de teste usando o modelo treinado.
y_pred = clf.predict(X_test)