import pandas as pd
import numpy as np

# ATIVIDADE 2
df = pd.read_excel("vendas_roupas1.xlsx")
print(df)

categoria = df["Categoria"]
quantidade_vendida = df["Quantidade Vendida"]
print("\n", quantidade_vendida.describe()) # describe descreve informacoes do conjunto
print("\n", categoria.describe())
print("\n", categoria.unique()) # unique traz categorias sem repeticao

q1 = np.quantile(quantidade_vendida, 0.25)
q2 = np.quantile(quantidade_vendida, 0.50)
q3 = np.quantile(quantidade_vendida, 0.75)

print("\nQ1:", q1)
print("Q2:", q2)
print("Q3:", q3)

media = np.mean(quantidade_vendida)
mediana = np.median(quantidade_vendida)

print("\nMédia: ", media)
print("Mediana:", mediana)

# Calculando com ordenação
qtdvdd_organizada = df.sort_values(by="Quantidade Vendida", ascending=True)
quantidade_vendida = qtdvdd_organizada["Quantidade Vendida"]
print("\n", quantidade_vendida.values)
