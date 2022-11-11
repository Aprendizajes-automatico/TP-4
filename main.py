import numpy as np
import pandas as pd
from kMedias import poner_clase_aleatoria, kMedias
from utils import sacar_clase_primaria_pd, estandarizar_atributos, quedarse_valores_clase_primaria
from AgrupamientoJerarquico import agrupamiento_jerarquico, criterio_minimo, criterio_maximo, plotear_agrupamiento
from Kohonen import Kohonen, KohonenEtiquetar
import som as SOM

conjunto = pd.read_csv("acath2.csv", encoding= 'unicode_escape')
iris = pd.read_csv("Iris.csv", encoding= 'unicode_escape')
actual_Y = conjunto.iloc[:, -1]
actual_X = sacar_clase_primaria_pd(conjunto)
# Reemplaza los vacíos por NaN
actual_X["choleste"].replace('', np.nan, inplace=True)
# Borra los NaN
actual_X.dropna(subset=['choleste'], inplace=True)
k = 2
actual_con_clase_aleatoria = poner_clase_aleatoria(actual_X, k)
actual_estandarizado = estandarizar_atributos(actual_con_clase_aleatoria, ['age', 'cad.dur', 'choleste' ]).to_numpy()
#agrupamiento_k_medias = kMedias(actual_estandarizado, k)
#print(agrupamiento_k_medias)
agrupamiento_jerarquico(actual_estandarizado, criterio_minimo)
#agrupamiento_jerarquico(actual_estandarizado, criterio_maximo)
#plotear_agrupamiento(actual_estandarizado)
"""
print("------------------")
pesos = Kohonen(actual_estandarizado)
KohonenEtiquetar(actual_estandarizado, pesos)

pesos = Kohonen(iris.to_numpy())
KohonenEtiquetar(iris.to_numpy(), pesos)
"""
