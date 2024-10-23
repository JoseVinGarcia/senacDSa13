import pandas as pd
import numpy as np

# CALCULANDO MÉDIA DE SALÁRIOS
media = (2000 + 2500 + 3000 + 3500 + 4000 + 30000) / 6
print("\nMédia calculada normal:", media)

# essa média não pode ser considerada confiável, pois o 30.000 puxa muito a média para cima (chamada outlier)

# CALCULANDO MÉDIA COM NUMPY
dados_salario = [2000, 2500, 3000, 3500, 4000, 30000]

media = np.mean(dados_salario)
print("Média com Numpy:", media)

# CALCULANDO MEDIANA COM NUMPY
dados_salario = [2000, 2500, 3000, 3500, 4000, 30000]

mediana = np.median(dados_salario)
print("Mediana com numpy:", mediana)
