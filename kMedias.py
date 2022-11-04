import random
import numpy as np
from utils import quedarse_valores_clase_primaria, sacar_clase_primaria_pd, filtrar_por_clase_primaria_v2, sacar_clase_primaria_v2

def poner_clase_aleatoria(conjunto, k):
    lista_clases = []
    for i in range(len(conjunto)):
        lista_clases.append(random.randrange(k))
    return conjunto.assign(sigdz=lista_clases)

def kMediasNp(conjunto_original, k, conjunto_actualizado=np.zeros(0)):
    # Lista de centroides
    # Cantidad de columnas del conjunto, en el ejemplo son 4. Se le resta 1 para sacarle la clase primaria
    cantidad_columnas = conjunto_original.shape[1] - 1

    while not np.all(conjunto_original == conjunto_actualizado):
        print("Itero")
        centroides = []
        if not conjunto_actualizado:
            conjunto_actualizado = conjunto_original 
        else:
            conjunto_original = conjunto_actualizado
        for i in range(k):
            resultados_centroide_xi = []
            # Por cada iteración se queda con la clase que le digamos.
            conjuntos_clase_i = filtrar_por_clase_primaria_v2(conjunto_original, i)
            # Para hacer el algoritmo, sacamos la clase primaria
            conjuntos_i_sin_clase_primaria = sacar_clase_primaria_v2(conjuntos_clase_i)

            # Se pone el -1 para no iterar la clase primaria
            for columna in range(cantidad_columnas):
                #Sumamos todos los xi de cada columna 
                suma_total_columna = conjuntos_i_sin_clase_primaria[:,columna].sum()
                # Se calcula la posición del centroide            
                resultados_centroide_xi.append(suma_total_columna / len(conjuntos_i_sin_clase_primaria))
            centroides.append(resultados_centroide_xi)
        print(centroides)
        nuevas_clases = []
        # Por fila
        print(len(conjunto_original))
        for i in range(len(conjunto_original)):
            # Distancias por fila
            distancias = np.zeros(len(centroides))
            # Valores del centroide
            for c, centroide in enumerate(centroides):
                # Valor de la columna
                for j in range(cantidad_columnas):
                    distancias[c] += pow((abs(centroide[j] - conjunto_original[i,j])), 2)
                
            distancias = list(map(lambda distancia: np.sqrt(distancia), distancias))
            print(distancias)
            #conjunto_actualizado[i,cantidad_columnas]= distancias.index(min(distancias))
            conjunto_actualizado[i,4] = distancias.index(min(distancias))
            nuevas_clases.append(distancias.index(min(distancias)))
    #print(nuevas_clases)
    return conjunto_actualizado