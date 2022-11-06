from utils import sacar_clase_primaria_v2, obtener_distancias, eliminar_fila_columna
import numpy as np

def agrupamiento_jerarquico(conjunto, criterio):
    #conjunto = sacar_clase_primaria_v2(conjunto)

    matriz_distancias = np.zeros((len(conjunto), len(conjunto)))
    # Valor, punto1 , punto2
    primeros_grupos = []
    for i, punto1 in enumerate(conjunto):
        for j, punto2 in enumerate(conjunto):
            # Obtengo la distancia de un punto al otro y lo guardo en la matriz
            matriz_distancias[i,j] = obtener_distancias(punto1, [punto2])[0]
    print(matriz_distancias)
    while (len(matriz_distancias) != 1):
        minimo = obtener_minimo(matriz_distancias)
        valor, fila1, fila2 = minimo
        distancias = criterio(matriz_distancias, fila1, fila2)
        matriz_distancias[fila1] = distancias
        primeros_grupos.append([valor, f'({fila1} - {fila2})'])
        matriz_distancias = eliminar_fila_columna(matriz_distancias, fila2)
        print("--------------------")
        print(minimo)
        print(matriz_distancias)
        print("--------------------")
    print(primeros_grupos)
    print(matriz_distancias)

def obtener_minimo(matriz):
    minimo = [999,0,0]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            distancia = matriz[i,j]
            if(distancia != 0 and distancia < minimo[0]):
                minimo = [distancia, i, j]
    return minimo

def criterio_minimo(matriz, fila1, fila2):
    distancias_minimas = []
    for i in range(np.shape(matriz)[1]):
        x = matriz[fila1][i]
        y = matriz[fila2][i]
        distancias_minimas.append(x if x <= y else y)
    return distancias_minimas

