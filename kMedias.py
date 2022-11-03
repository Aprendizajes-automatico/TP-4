import random
import numpy as np
from utils import quedarse_valores_clase_primaria, sacar_clase_primaria_pd, filtrar_por_clase_primaria_v2, sacar_clase_primaria_v2

def poner_clase_aleatoria(conjunto, k):
    lista_clases = []
    for i in range(len(conjunto)):
        lista_clases.append(random.randrange(k))
    return conjunto.assign(sigdz=lista_clases)

def kMediasNp(conjunto_original, k, conjunto_actualizado, iter=0):
    conjunto_original_clase_primaria = quedarse_valores_clase_primaria(conjunto_original)
    conjunto_actualizado_clase_primaria = quedarse_valores_clase_primaria(conjunto_actualizado)
    centroides = []
    print(conjunto_original_clase_primaria)
    print(conjunto_actualizado_clase_primaria)
    # Cantidad de columnas del conjunto, en el ejemplo son 4. Se le resta 1 para sacarle la clase primaria
    cantidad_columnas = conjunto_original.shape[1] - 1
    if(np.all(conjunto_original == conjunto_actualizado) and iter != 0):
        return conjunto_actualizado
    else:
        for i in range(k):
            # Por cada iteración se queda con la clase que le digamos.
            centroide_clase_i = filtrar_por_clase_primaria_v2(conjunto_actualizado, i)
            # Para hacer el algoritmo, sacamos la clase primaria
            centroide_sin_clase_primaria = sacar_clase_primaria_v2(centroide_clase_i)
            suma_total_columna_xi = []

            # Se pone el -1 para no iterar la clase primaria
            for columna in range(cantidad_columnas):
                #Sumamos todos los xi de cada columna 
                suma_total_columna_xi.append(centroide_sin_clase_primaria[:,columna].sum())
            # Se calcula la posición del centroide
            centroides.append(list(map(lambda x: x / len(centroide_sin_clase_primaria), suma_total_columna_xi)))
        
        nuevas_clases = []
        # Por fila
        for i in range(len(conjunto_actualizado)):
            # Distancias por fila
            distancias = np.zeros(len(centroides))
            # Valores del centroide
            for c, centroide in enumerate(centroides):
                # Valor de la columna
                for j in range(cantidad_columnas):
                    distancias[c] += (centroide[j] - conjunto_actualizado[i,j]) ** 2
                
            distancias = list(map(lambda distancia: distancia ** 1/2, distancias))
            #conjunto_actualizado[i,cantidad_columnas]= distancias.index(min(distancias))
            conjunto_actualizado[i,4] = distancias.index(min(distancias))
            nuevas_clases.append(distancias.index(min(distancias)))
        """
        print(quedarse_valores_clase_primaria(conjunto_original))
        print("--------------------")    
        print(quedarse_valores_clase_primaria(conjunto_actualizado))
        print(quedarse_valores_clase_primaria(conjunto_original) == quedarse_valores_clase_primaria(conjunto_actualizado) )
        """
        kMediasNp(conjunto_original, k, conjunto_actualizado, iter+1)

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