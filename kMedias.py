import random
import numpy as np
from utils import obtener_distancias, filtrar_por_clase_primaria_np, sacar_clase_primaria_np

def poner_clase_aleatoria(conjunto, k):
    lista_clases = []
    for i in range(len(conjunto)):
        lista_clases.append(random.randrange(k))
    return conjunto.assign(sigdz=lista_clases)


def kMedias(conjunto_original, k, iter_max = 100):
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
        conjunto_sin_clase_primaria = sacar_clase_primaria_np(conjunto_original)
        # Itera por cantidad totales de filas. Son todos los datos del conjunto
        for i in range(len(conjunto_sin_clase_primaria)):
            distancias = obtener_distancias(conjunto_original[i], centroides)
            # Se queda con el valor mas chico y lo pone el como clase primaria a la fila que está iterando
            conjunto_actualizado[i, cantidad_columnas] = distancias.index(min(distancias))
        iter += 1
    return conjunto_actualizado

def obtener_centroides(conjunto_original, cantidad_columnas, k):
    centroides = []
    for k in range(k):
        conjunto_clase_k = filtrar_por_clase_primaria_np(conjunto_original, k)
        conjunto_clase_k_sin_primaria = sacar_clase_primaria_np(conjunto_clase_k)
        centroide_xi = []
        for indice_columna in range(cantidad_columnas):
            suma_total_columna = conjunto_clase_k_sin_primaria[:,indice_columna].sum()
            centroide_xi.append(suma_total_columna / len(conjunto_clase_k_sin_primaria))
        centroides.append(centroide_xi)
    return centroides

def obtener_accurracy_kMedias(pred_Y, actual_Y):
    for clase in np.unique(pred_Y):
        indices_clase = [i for (i, pred) in enumerate(pred_Y) if pred == int(clase)]
        cantidad_enfermos = sum([0 if (i not in indices_clase or actual_Y[i] == 0) else 1  for i in range(len(actual_Y))])
        print(f"La clase {clase} tiene una probabilidad de {round(cantidad_enfermos / len(indices_clase) * 100, 2)}% tener la enfermedad. ")