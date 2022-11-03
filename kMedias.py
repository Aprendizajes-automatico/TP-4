import random
import numpy as np
from utils import filtrar_por_clase_primaria, sacar_clase_primaria_pd

def poner_clase_aleatoria(conjunto, k):
    lista_clases = []
    for i in range(len(conjunto)):
        lista_clases.append(random.randrange(k))
    return conjunto.assign(sigdz=lista_clases)

def kMedias(conjunto_original, k, conjunto_actualizado=[]):
    centroides = []
    columnas = sacar_clase_primaria_pd(conjunto_original).columns
    #Convertimos a np para trabajar mas fácil
    conjunto_np = conjunto_original.to_numpy()
    #print(list(filter(lambda x: not x , ((conjunto == conjunto).all()))))
    #Itera por cada k
    for i in range(k):
        # Por cada iteración se queda con la clase que le digamos.
        centroide_clase_i = filtrar_por_clase_primaria(conjunto_original, i)
        # Para hacer el algoritmo, sacamos la clase primaria
        centroide_sin_clase_primaria = sacar_clase_primaria_pd(centroide_clase_i)
        # 
        suma_total_columna_xi = []

        for columna in columnas:
            suma_total_columna_xi.append(centroide_sin_clase_primaria[columna].sum())

        centroides.append(list(map(lambda x: x / len(centroide_sin_clase_primaria), suma_total_columna_xi)))
    
    print(centroides)
    #
    nuevas_clases = np.zeros(len(conjunto_np))
    # Por fila
    for i in range(len(conjunto_np)):
        # Distancias por fila
        distancias = np.zeros(len(centroides))
        # Valores del centroide
        for c, centroide in enumerate(centroides):
            # Valor de la columna
            for j in range(len(columnas)):
                distancias[c] += (centroide[j] - conjunto_np[i,j]) ** 2
            
        distancias = list(map(lambda distancia: distancia ** 1/2, distancias))
        conjunto_np[i,len(columnas)]= distancias.index(min(distancias))
        nuevas_clases[i] = distancias.index(min(distancias))
    print(conjunto_np)


"""
import random
import numpy as np
from utils import filtrar_por_clase_primaria, sacar_clase_primaria_np

def poner_clase_aleatoria(conjunto, k):
    lista_clases = []
    for i in range(len(conjunto)):
        lista_clases.append(random.randrange(k))
    return conjunto.assign(sigdz=lista_clases)

def kMedias(conjunto_original, columnas, k, conjunto_actualizado=np.array(0)):
    centroides = []
    #Convertimos a np para trabajar mas fácil
    if(np.all(conjunto_original == conjunto_actualizado)):
        print(conjunto_actualizado)
        return conjunto_actualizado;
    else:
        if(conjunto_actualizado == [0]):
            conjunto_actualizado = conjunto_original
        #Itera por cada k
        for i in range(k):
            # Por cada iteración se queda con la clase que le digamos.
            centroide_clase_i = filtrar_por_clase_primaria(conjunto_actualizado, i)
            # Para hacer el algoritmo, sacamos la clase primaria
            centroide_sin_clase_primaria = sacar_clase_primaria_np(centroide_clase_i)
            # 
            suma_total_columna_xi = []

            for columna in range(len(columnas)):
                suma_total_columna_xi.append(centroide_sin_clase_primaria[:,columna].sum())

            centroides.append(list(map(lambda x: x / len(centroide_sin_clase_primaria), suma_total_columna_xi)))
        
        #print(centroides)
        # Por fila
        for i in range(len(conjunto_actualizado)):
            # Distancias por fila
            distancias = np.zeros(len(centroides))
            # Valores del centroide
            for c, centroide in enumerate(centroides):
                # Valor de la columna
                for j in range(len(columnas)):
                    distancias[c] += (centroide[j] - conjunto_actualizado[i,j]) ** 2
                
            distancias = list(map(lambda distancia: distancia ** 1/2, distancias))
            conjunto_actualizado[i,len(columnas)]= distancias.index(min(distancias))            
        return kMedias(conjunto_original, k, conjunto_actualizado)

"""