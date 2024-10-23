import pandas as pd
import numpy as np

# QUARTIL
# MÉTODO 1
idades = np.array([12,15,17,20,22,25,28,30,35,40])

# 25%, 50% e 75% das idades
q1 = np.quantile(idades, 0.25)
q2 = np.quantile(idades, 0.50)
q3 = np.quantile(idades, 0.75)

print("Q1 (25% das idades está abaixo de):",q1)
print("Q2 (50% das idades estão abaixo de e acima de):",q2)
print("Q3 (75% dos meus dados são inferiores à):",q3)
