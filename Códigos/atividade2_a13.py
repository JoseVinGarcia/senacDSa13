import pandas as pd
import numpy as np

# ATIVIDADE 2
print("="*90)

df = pd.read_excel("vendas_eletos_eletronicos2.xlsx")
print(df)

total_vendas = df["Total"]

# Calculando os valores centrais
media_totais = np.mean(total_vendas)
mediana_totais = np.median(total_vendas)

# 1. VALORES CENTRAIS
print("\nMÉDIA DE TOTAIS:", media_totais)
print("MEDIANA DE TOTAIS:", mediana_totais)
print("Novamente, usaremos a mediana como medida de base, por uma alteração muito extrema de valores.")

# 2. QUANTIS
q1 = np.quantile(total_vendas,0.25)
q2 = np.quantile(total_vendas,0.50)
q3 = np.quantile(total_vendas,0.75)

print(f"\nQ1 DE TOTAL DE VENDAS: {q1}. Ou seja, 25% das vendas estão abaixo de {q1}")
print(f"Q2 DE TOTAL DE VENDAS: {q2}. Ou seja, 50% das vendas estão abaixo de {q2} e 50% estão acima desse valor.")
print(f"Q3 DE TOTAL DE VENDAS: {q3}. Ou seja, 75% das vendas estão abaixo de {q3}\n")

# 3. MAIS VENDIDOS
total_organizado = df.sort_values(by="Total", ascending=False)
print("PRODUTOS MAIS VENDIDOS:")
print(total_organizado[["Nome do Produto","Total"]])
