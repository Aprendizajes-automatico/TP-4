from utils import imprimir_matriz, obtener_distancias, eliminar_fila_columna, poner_ceros_en_fila_columna, sacar_clase_primaria_np, obtener_valores_en_conjunto, flattenList
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
        # Obtengo el índice del merge que voy a hacer entre 2 grupos
        indice_nuevo_grupo = len(grupos)
        # Obtengo el mínimo    
        distancia, fila1, fila2 = obtener_minimo(matriz_distancias)
        nombre_nuevo_grupo = f'({fila1} - {fila2})'
        # Se repite pero porque estos son los indices
        indices_filas_del_nuevo_grupo = [fila1, fila2]
        # Este if se hace para preguntar si estás uniendo con un grupo ya existente (4-5) -> (4-5-3)
        if(fila2 >= len(conjunto)):
            grupo_a_mergear_1 = grupos[fila1]
            grupo_a_mergear_2 = grupos[fila2]
            nombre_grupo_a_unir = grupo_a_mergear_2['nombre']
            nombre_nuevo_grupo = f'({nombre_grupo_a_unir} - {grupos[fila1]})'
            indices_filas_del_nuevo_grupo = [*grupo_a_mergear_2['indices'], fila1]
        nuevo_grupo = {
            'nombre': nombre_nuevo_grupo,
            'distancia': distancia,
            'key': indice_nuevo_grupo,
            'indices': indices_filas_del_nuevo_grupo
        }
        grupos.append(nuevo_grupo)
        print(fila1, " - ", fila2)
        #print(grupos)
        imprimir_matriz(matriz_distancias)
        distancias = criterio(matriz_distancias, fila1, fila2, grupos, conjunto)
        matriz_distancias[indice_nuevo_grupo] = distancias
        matriz_distancias = poner_ceros_en_fila_columna(matriz_distancias, [fila1, fila2])       
        print("-----------------")
      
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

def criterio_minimo(matriz, fila1, fila2, _ , __):
    distancias_minimas = []
    for i in range(np.shape(matriz)[1]):
        x = matriz[fila1][i]
        y = matriz[fila2][i]
        distancias_minimas.append(x if x < y else y)
    return distancias_minimas

def criterio_maximo(matriz, fila1, fila2, _, __):
    distancias_maximas = []
    for i in range(np.shape(matriz)[1]):
        x = matriz[fila1][i]
        y = matriz[fila2][i]
        if (x == 0 or y == 0):
            distancias_maximas.append(0)
        else:
            distancias_maximas.append(x if x > y else y)
    return distancias_maximas

def criterio_centroide(matriz, fila1, fila2, grupos, conjunto):        
    indices_valores_grupo = [*grupos[fila1]['indices'], *grupos[fila2]['indices']]
    valores_grupo = obtener_valores_en_conjunto(conjunto, indices_valores_grupo)
    centroide_nuevo_grupo = obtener_centroide(valores_grupo)
    distancias = []
    for i in range(len(matriz[0])):
        try:
            valores_a_comparar = obtener_valores_en_conjunto(conjunto, grupos[i]['indices'])
            if(np.sum(matriz[i]) != 0 and i != fila1 and i != fila2):
                centroide_a_comparar = obtener_centroide(valores_a_comparar)
                distancias.append(obtener_distancias(centroide_nuevo_grupo, [centroide_a_comparar]))
        except IndexError:
            pass
    for _ in range(len(matriz) - len(distancias)):
        distancias.append([0])

    print(distancias)
    return flattenList(distancias)

def obtener_centroide(valores_grupo):
    centroide = []
    for indice_columna in range(len(valores_grupo[0]) - 1):
        suma_total_columna = valores_grupo[:,indice_columna].sum()
        centroide.append(suma_total_columna / len(valores_grupo))
    return centroide

def plotear_agrupamiento(conjunto):
    conjunto_a_plotear = sacar_clase_primaria_np(conjunto)
    dendrogram = sch.dendrogram(sch.linkage(conjunto_a_plotear, method = 'centroid'))
    plt.title('Dendograma')
    plt.xlabel('Indice - Fila')
    plt.ylabel('Distancia')
    plt.show()