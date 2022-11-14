import numpy as np
import pandas as pd
from kMedias import poner_clase_aleatoria, kMedias, obtener_accurracy_kMedias
from utils import sacar_clase_primaria_pd, estandarizar_atributos, quedarse_valores_clase_primaria,sacar_clase_primaria_np
from AgrupamientoJerarquico import agrupamiento_jerarquico, criterio_minimo, criterio_maximo, plotear_agrupamiento, criterio_centroide
from Kohonen import Kohonen, KohonenEtiquetar
import matplotlib.pyplot as plt

conjunto = pd.read_csv("acath.csv", encoding= 'unicode_escape')
iris = pd.read_csv("Iris.csv", encoding= 'unicode_escape')
# Reemplaza los vacíos por NaN
conjunto["choleste"].replace('', np.nan, inplace=True)
# Borra los NaN
conjunto.dropna(subset=['choleste'], inplace=True)
actual_Y = conjunto.iloc[:, -1]
actual_X = sacar_clase_primaria_pd(conjunto)
k = 2
actual_con_clase_aleatoria = poner_clase_aleatoria(actual_X, k)
#actual_estandarizado = estandarizar_atributos(actual_con_clase_aleatoria, ['age', 'cad.dur', 'choleste' ]).to_numpy()
actual_estandarizado = estandarizar_atributos(actual_con_clase_aleatoria, ['cad.dur', 'choleste' ]).to_numpy()
agrupamiento_k_medias = kMedias(actual_estandarizado, k)
obtener_accurracy_kMedias(quedarse_valores_clase_primaria(agrupamiento_k_medias), actual_Y.to_list())
#agrupamiento_jerarquico(actual_estandarizado, criterio_minimo)
#agrupamiento_jerarquico(actual_estandarizado, criterio_maximo)
#agrupamiento_jerarquico(actual_estandarizado, criterio_centroide)
#plotear_agrupamiento(actual_estandarizado)

"""
a_plotear = sacar_clase_primaria_np(actual_estandarizado)
X = a_plotear[:,0]
Y = a_plotear[:,-1]
print(a_plotear)
plt.plot(X, Y, 'o')
plt.show()

print("------------------")
pesos = Kohonen(actual_estandarizado)
KohonenEtiquetar(actual_estandarizado, pesos)

pesos = Kohonen(iris.to_numpy())
KohonenEtiquetar(iris.to_numpy(), pesos)
"""
