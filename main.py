import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Carregar o dataset local (ex: após baixar do Kaggle)
df = pd.read_csv('us_house_Sales_data.csv')

# 2. Pré-processamento simples
df_limpo = df.select_dtypes(include='number').dropna()

# 3. Aplicar KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(df_limpo)
df_limpo['grupo'] = kmeans.labels_

# 4. Visualizar (usando as duas primeiras colunas numéricas)
plt.scatter(df_limpo.iloc[:, 0], df_limpo.iloc[:, 1], c=df_limpo['grupo'])
plt.title("Agrupamento de dados com KMeans")
plt.xlabel(df_limpo.columns[0])
plt.ylabel(df_limpo.columns[1])
plt.show()

df = pd.read_csv('us_house_Sales_data.csv')
