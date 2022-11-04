import numpy as np
import pandas as pd
from kMedias import poner_clase_aleatoria, kMediasNp
from utils import sacar_clase_primaria_pd, estandarizar_atributos, quedarse_valores_clase_primaria

conjunto = pd.read_csv("acath.csv", encoding= 'unicode_escape')
actual_Y = conjunto.iloc[:, -1]
actual_X = sacar_clase_primaria_pd(conjunto)
# Reemplaza los vacíos por NaN
actual_X["choleste"].replace('', np.nan, inplace=True)
# Borra los NaN
actual_X.dropna(subset=['choleste'], inplace=True)
k = 2
actual_con_clase_aleatoria = poner_clase_aleatoria(actual_X, k)
actual_estandarizado = estandarizar_atributos(actual_con_clase_aleatoria, ['age', 'cad.dur', 'choleste' ]).to_numpy()
agrupamiento_k_medias = kMediasNp(actual_estandarizado, k)
print("-----------")
print(quedarse_valores_clase_primaria(actual_estandarizado))
print(quedarse_valores_clase_primaria(agrupamiento_k_medias))


