import numpy as np
import pandas as pd
from kMedias import poner_clase_aleatoria, kMedias
from utils import sacar_clase_primaria_pd

conjunto = pd.read_csv("acath.csv", encoding= 'unicode_escape')
actual_Y = conjunto.iloc[:, -1]
actual_X = sacar_clase_primaria_pd(conjunto)
# Reemplaza los vacíos por NaN
actual_X["choleste"].replace('', np.nan, inplace=True)
# Borra los NaN
actual_X.dropna(subset=['choleste'], inplace=True)

k = 2

actual_con_clase_aleatoria = poner_clase_aleatoria(actual_X, k)
kMedias(actual_con_clase_aleatoria, k)

"""
import numpy as np
import pandas as pd
from kMedias import poner_clase_aleatoria, kMedias
from utils import sacar_clase_primaria_pd

conjunto = pd.read_csv("acath.csv", encoding= 'unicode_escape')
actual_Y = conjunto.iloc[:, -1]
actual_X = sacar_clase_primaria_pd(conjunto)
columnas = actual_X.keys()
# Reemplaza los vacíos por NaN
actual_X["choleste"].replace('', np.nan, inplace=True)
# Borra los NaN
actual_X.dropna(subset=['choleste'], inplace=True)

k = 2

actual_con_clase_aleatoria = poner_clase_aleatoria(actual_X, k).to_numpy()
kMedias(actual_con_clase_aleatoria, columnas, k)


"""


