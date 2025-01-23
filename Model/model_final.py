import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Clustering e métricas de distância
from sklearn.cluster import KMeans
from scipy.spatial import distance

# Pré-processamento
from sklearn.preprocessing import OneHotEncoder

# Avaliação do modelo
from sklearn.metrics import silhouette_score

# Pipeline e redução dimensional
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Método do cotovelo para KMeans
from yellowbrick.cluster import KElbowVisualizer

# Configuração para exibir todas as colunas
pd.set_option('display.max_columns', None)


df = pd.read_csv('../data/marketing_campaign_clean.csv').dropna()
df.drop(['Dt_Customer', 'Year', 'Month', 'Day', 'SeniorityDays', 'Date'], axis=1, inplace=True)

print(df.shape)
print(df.info())
df.head()

# Selezione delle colonne numeriche
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
features = numerical_cols.drop("ID")

# Standardizzazione dei dati
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

# PCA con tutti i componenti
pca_full = PCA()
pca_full.fit(X_scaled)

# Varianza spiegata
explained_variance = pca_full.explained_variance_ratio_

# Grafico della varianza spiegata cumulativa
plt.figure(figsize=(8, 6))
plt.plot(range(1, len(explained_variance) + 1), np.cumsum(explained_variance), marker='o', linestyle='--')
plt.title('Varianza Spiegata Cumulativa')
plt.xlabel('Numero di Componenti')
plt.ylabel('Varianza Spiegata Cumulativa (%)')
plt.axhline(y=0.85, color='r', linestyle='--', label='85% soglia')
plt.axhline(y=0.95, color='g', linestyle='--', label='95% soglia')
plt.legend()
plt.grid()
plt.show()

# Determinare il numero minimo di componenti per una soglia
threshold = 0.85  # Cambia a 0.95 se necessario
optimal_components = np.argmax(np.cumsum(explained_variance) >= threshold) + 1
print(f"Numero di componenti che spiegano almeno l'85% della varianza: {optimal_components}")

# PCA
pca = PCA(random_state=42, n_components=15)
principal_components = pca.fit_transform(X_scaled)

# Creazione del DataFrame con i risultati
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 
                                                          'PC8', 'PC9', 'PC10', 'PC11', 'PC12', 'PC13', 'PC14', 'PC15'])
pca_df['ID'] = df['ID']

df_model = pca_df.drop('ID', axis=1)
padronizador = StandardScaler()
df_padronizado = padronizador.fit_transform(df_model)

num_features = list(df_model.select_dtypes('number').columns)
cat_features = list(df_model.select_dtypes('object').columns)

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(drop='first', sparse_output=False), cat_features)  # Drop='first' para evitar multicolinearidade
    ])

X_preprocessed = preprocessor.fit_transform(df_model)

kmeans = KMeans(n_clusters=4, max_iter=600, algorithm = 'lloyd', random_state=42)
kmeans.fit(X_preprocessed)
df['grupo'] = kmeans.labels_
df_model['grupo'] = kmeans.labels_

