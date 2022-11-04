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
    # Inicializa el conjunto_actualizado vacío -> []
    conjunto_actualizado = np.zeros(0)
    # Shape devuelve (x,y) x = cantidad filas; y = cantidad de columnas; shape[0] -> x; shape[1] -> y;
    cantidad_columnas = conjunto_original.shape[1] - 1
    # Mientras los conjuntos no sean iguales y no cumpla con las iteraciones, entra
    while (not np.all(conjunto_actualizado == conjunto_original) and iter <= iter_max):
        print("Iter: ", iter)
        # Si es la primera vez que entra al while, iguala los conjuntos.        
        if(conjunto_actualizado.all()):
            conjunto_actualizado = np.copy(conjunto_original)
        # Si no, actualiza el "original" con los nuevos valores después de haberlo evaluado con el centroide
        else:
            conjunto_original = np.copy(conjunto_actualizado)
        # Obtiene los valores de los centroides. Esto devuelve una lista de K Centroides -> [[1,2,3,4], [4,5,6,7]]
        centroides = obtener_centroides(conjunto_original, cantidad_columnas, k)
        #Saca la columna de la clase primaria. (Tiene que ser la última de la derecha)
        conjunto_sin_clase_primaria = sacar_clase_primaria_v2(conjunto_original)
        # Itera por cantidad totales de filas. Son todos los datos del conjunto
        for i in range(len(conjunto_sin_clase_primaria)):
            # k = 2 -> [0,0]
            distancias = np.zeros(len(centroides))
            # Centroide es una lista de los valores centroides
            for c, centroide in enumerate(centroides):
                # Indice de cada columna -> 4
                for j in range(cantidad_columnas):
                    # Fórmula para distancia entre 2 vectores. (un centroide y una fila de valores)                
                    distancias[c] += pow((conjunto_original[i,j] - centroide[j]), 2)
            # Aplica raiz cuadrada a los dos resultados de los centroides
            distancias = [abs(np.sqrt(distancia)) for distancia in distancias]
            # Se queda con el valor mas chico y lo pone el como clase primaria a la fila que está iterando
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