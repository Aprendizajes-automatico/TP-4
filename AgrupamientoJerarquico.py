from utils import imprimir_matriz, obtener_distancias, eliminar_fila_columna, poner_ceros_en_fila_columna, sacar_clase_primaria_np
import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

def agrupamiento_jerarquico(conjunto, criterio):
    numero_de_grupos = len(conjunto) * 2 - 1
    matriz_distancias = np.zeros((numero_de_grupos, numero_de_grupos))
    # Valor, punto1 , punto2
    grupos = [{'nombre': str(i), 'distancia': 0, 'key': i, 'indices': [i]} for i in range(len(conjunto))]

    for i, punto1 in enumerate(conjunto):
        for j, punto2 in enumerate(conjunto):
            # Obtengo la distancia de un punto al otro y lo guardo en la matriz
            matriz_distancias[i,j] = obtener_distancias(punto1, [punto2])[0]
    imprimir_matriz(matriz_distancias)
    while (numero_de_grupos != len(grupos)):
        # Obtengo el mínimo    
        distancia, fila1, fila2 = obtener_minimo(matriz_distancias)
        # Obtengo el índice del merge que voy a hacer entre 2 grupos
        indice_nuevo_grupo = len(grupos)
        distancias = criterio(matriz_distancias, fila1, fila2)
        matriz_distancias[indice_nuevo_grupo] = distancias
        matriz_distancias = poner_ceros_en_fila_columna(matriz_distancias, [fila1, fila2])       
        print("-----------------")
        imprimir_matriz(matriz_distancias)
        #matriz_distancias = eliminar_fila_columna(matriz_distancias, fila2)
        nombre_nuevo_grupo = f'({fila1} - {fila2})'
        indices_nuevo_grupo = [fila1, fila2]

        if(fila2 >= len(conjunto)):
            nombre_grupo_a_unir = grupos[fila2]['nombre']
            nombre_nuevo_grupo = f'({nombre_grupo_a_unir} - {fila1})'
        nuevo_grupo = {
            'nombre': nombre_nuevo_grupo,
            'distancia': distancia,
            'key': indice_nuevo_grupo
        }
        grupos.append(nuevo_grupo)
        print(fila1, " - ", fila2)
        print(grupos)
      
    print("-----------------")
    print(grupos)
    imprimir_matriz(matriz_distancias)

def obtener_minimo(matriz):
    minimo = [999,0,0]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            distancia = matriz[i,j]
            if(distancia != 0 and distancia < minimo[0]):
                # Se hace este if para que el i sea mas chico que el j
                if(i < j):
                    minimo = [distancia, i, j]
                else:
                    minimo = [distancia, j, i]
    return minimo

def criterio_minimo(matriz, fila1, fila2):
    distancias_minimas = []
    for i in range(np.shape(matriz)[1]):
        x = matriz[fila1][i]
        y = matriz[fila2][i]
        distancias_minimas.append(x if x < y else y)
    return distancias_minimas

def criterio_maximo(matriz, fila1, fila2):
    distancias_maximas = []
    for i in range(np.shape(matriz)[1]):
        x = matriz[fila1][i]
        y = matriz[fila2][i]
        if (x == 0 or y == 0):
            distancias_maximas.append(0)
        else:
            distancias_maximas.append(x if x > y else y)
    return distancias_maximas

def plotear_agrupamiento(conjunto):
    conjunto_a_plotear = sacar_clase_primaria_np(conjunto)
    dendrogram = sch.dendrogram(sch.linkage(conjunto_a_plotear, method = 'complete'))
    plt.title('Dendograma')
    plt.xlabel('Indice - Fila')
    plt.ylabel('Distancia')
    plt.show()