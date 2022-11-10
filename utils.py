import numpy as np
import math
import random

def filtrar_por_clase_primaria(conjunto, clase):
    return conjunto.where(conjunto['sigdz'] == clase)

def sacar_clase_primaria_pd(conjunto):
    return conjunto.iloc[:, :-1]

def sacar_clase_primaria_np(conjunto):
    return conjunto.iloc[:, :-1]

def filtrar_por_clase_primaria_v2(conjunto, clase):
    return conjunto[conjunto[:,-1] == clase]

def sacar_clase_primaria_v2(conjunto):
    return np.delete(conjunto, -1, axis=1)

def quedarse_valores_clase_primaria(conjunto):
    return conjunto[:,-1]

def estandarizar_atributos(conjunto, attribute_names):    
    for i, atributo in enumerate(attribute_names):
        nuevos_valores_estandarizados = []
        columna = conjunto[atributo] 
        # obtengo la media de los atributos elegidos
        media = columna.mean()
        desviacion = columna.std()        
        for valor in columna:
            nuevos_valores_estandarizados.append((valor - media) / desviacion)
        conjunto[atributo] = nuevos_valores_estandarizados        
    
    return conjunto    

def obtener_distancias(fila_valores, puntos):
    #cantidad_columnas = fila_valores.shape[1] - 1
    # k = 2 -> [0,0]
    distancias = np.zeros(len(puntos))
    # Puntos es una lista, [[x1,x2,x3,x4...,xn]]
    for p, punto in enumerate(puntos):
        # Indice de cada columna -> 4
        for j in range(len(fila_valores) - 1):
            # Fórmula para distancia entre 2 vectores. (un centroide y una fila de valores)                
            distancias[p] += pow((fila_valores[j] - punto[j]), 2)
    # Aplica raiz cuadrada a los dos resultados de los centroides
    distancias = [abs(np.sqrt(distancia)) for distancia in distancias]
    return distancias

def poner_ceros_en_fila_columna(conjunto, fila_columnas):
    nuevo_conjunto = np.copy(conjunto)
    for i in range(len(nuevo_conjunto)):
        for j in range(np.shape(nuevo_conjunto)[1]):
            if(np.isin(i, fila_columnas).any() or np.isin(j, fila_columnas).any()):
                nuevo_conjunto[i,j] = 0
    return nuevo_conjunto

def eliminar_fila_columna(conjunto, fila_columna):
    # Axis = 0 elimina la fila
    conjunto = np.delete(conjunto, fila_columna, axis=0)
    # Axis = 1 elimina la columna
    conjunto = np.delete(conjunto, fila_columna, axis=1)
    return conjunto

def obtener_conjuntos_de_datos(conjunto):
    p80 = len(conjunto) * 0.80
    p20 = len(conjunto) * 0.20
    return conjunto[:int(p80)], conjunto[-int(p20):]

def flattenList(list):
    return [item for sublist in list for item in sublist]

def imprimir_matriz(conjunto):
    with np.printoptions(precision=3, suppress=True):
        print(conjunto)

def multiplicar_listas(lista1, lista2):
	resultado = 0
	for i in range(len(lista1)):
		#w0*x0+w1*x1...+wn*xn
		resultado += lista1[i] * lista2[i]
	return resultado

def obtener_random(conjunto):
    return random.randint(0, len(conjunto) - 1)