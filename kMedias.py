import random
import numpy as np
from utils import quedarse_valores_clase_primaria, sacar_clase_primaria_pd, filtrar_por_clase_primaria_v2, sacar_clase_primaria_v2

def poner_clase_aleatoria(conjunto, k):
    lista_clases = []
    for i in range(len(conjunto)):
        lista_clases.append(random.randrange(k))
    return conjunto.assign(sigdz=lista_clases)


def kMediasNp(conjunto_original, k, iter_max = 100):
    iter = 0
    conjunto_actualizado = np.zeros(0)
    cantidad_columnas = conjunto_original.shape[1] - 1
    while (not np.all(conjunto_actualizado == conjunto_original) and iter <= iter_max):
        print("Iter: ", iter)
        if(conjunto_actualizado.all()):
            conjunto_actualizado = np.copy(conjunto_original)
        else:
            conjunto_original = np.copy(conjunto_actualizado)
        centroides = obtener_centroides(conjunto_original, cantidad_columnas, k)
        conjunto_sin_clase_primaria = sacar_clase_primaria_v2(conjunto_original)
        for i in range(len(conjunto_sin_clase_primaria)):
            distancias = np.zeros(len(centroides)) # k = 2 -> [0,0]
            for c, centroide in enumerate(centroides):
            # Valor de la columna
                for j in range(cantidad_columnas):                
                    distancias[c] += pow((conjunto_original[i,j] - centroide[j]), 2)
            distancias = [abs(np.sqrt(distancia)) for distancia in distancias]
            conjunto_actualizado[i, cantidad_columnas] = distancias.index(min(distancias))
        iter += 1
    return conjunto_actualizado

def obtener_centroides(conjunto_original, cantidad_columnas, k):
    centroides = []
    for k in range(k):
        conjunto_clase_k = filtrar_por_clase_primaria_v2(conjunto_original, k)
        conjunto_clase_k_sin_primaria = sacar_clase_primaria_v2(conjunto_clase_k)
        centroide_xi = []
        for indice_columna in range(cantidad_columnas):
            suma_total_columna = conjunto_clase_k_sin_primaria[:,indice_columna].sum()
            centroide_xi.append(suma_total_columna / len(conjunto_clase_k_sin_primaria))
        centroides.append(centroide_xi)
    return centroides