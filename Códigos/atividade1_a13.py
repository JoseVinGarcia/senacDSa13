import pandas as pd
import numpy as np

# ATIVIDADE 1
dados_casa = [150000,180000,200000,220000,250000,280000,300000,320000,400000,1500000]
media = np.mean(dados_casa)
mediana = np.median(dados_casa)

print("Média:", media)
print("Mediana:", mediana)

print("\nO valor mais representativo é a mediana, pois temos um valor muito extremo para calcular a média.")
