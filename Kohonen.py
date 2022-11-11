import numpy as np
from utils import sacar_clase_primaria_np, obtener_random, obtener_distancias, quedarse_valores_clase_primaria
from math import e

def Kohonen(conjunto):
    cantidad_neuronas = 5
    R_inicial = cantidad_neuronas
    R = R_inicial
    eta = 0.1
    epocas = 0
    cantidad_N = np.shape(conjunto)[1]
    epocas_maximas = 300 * cantidad_N    
    # Actualizar pesos con valores aleatorios del conjunto
    pesos = inicializar_pesos(conjunto, cantidad_neuronas)
    print(pesos)
    print("----------")
    while epocas < epocas_maximas:
        for _ in range(len(conjunto)):
            indice_random = obtener_random(conjunto)
            fila_random = conjunto[indice_random]
            distancias_neuronas_con_aleatorio = obtener_distancias_por_un_punto(fila_random, pesos)
            i , j = obtener_neurona_ganadora(distancias_neuronas_con_aleatorio)            
            pesos[i][j] = list(actualizar_peso_neurona(pesos[i][j], fila_random, eta))            
            pesos = actualizar_pesos_neuronas_vecinas(pesos, fila_random, [i,j], eta, R)            
        epocas += 1
        R = (epocas_maximas - epocas)*R_inicial/epocas_maximas        
        eta = 0.1 * (1 - epocas/epocas_maximas)
        print(R)
    print("----------")
    print(pesos)
    return pesos

def KohonenEtiquetar(conjunto, pesos):
    conjunto_a_etiquetar = np.copy(conjunto)
    clase_primaria = quedarse_valores_clase_primaria(conjunto)
    clases_posibles = np.unique(clase_primaria)
    lista_vacia_clases = list(np.zeros(len(clases_posibles)))    
    etiquetas = [[np.copy(lista_vacia_clases) for j in range(0, len(pesos))] for i in range(0, len(pesos))]
    for fila in conjunto_a_etiquetar:
        distancias_neuronas = obtener_distancias_por_un_punto(fila, pesos)
        i , j = obtener_neurona_ganadora(distancias_neuronas)        
        clase = fila[-1]
        indice_de_clase = list(clases_posibles).index(clase)
        etiquetas[i][j][indice_de_clase] += 1
    
    print(etiquetas)
    for clase in clases_posibles:
        print("Para clase " + str(clase) + "\n")
        for i in range(len(etiquetas)):
            for j in range(len(etiquetas)):
                cantidad_totales = sum(etiquetas[i][j])                
                if(cantidad_totales == 0):
                    print("0", end=" ")
                else:
                    indice_de_clase = list(clases_posibles).index(clase)
                    print(str(round(etiquetas[i][j][indice_de_clase] / (cantidad_totales),2 )) , end=" ")
            print("\n")


def inicializar_pesos(conjunto, cantidad_neuronas):
    nuevo_conjunto = sacar_clase_primaria_np(conjunto)
    pesos = [[[] for j in range(0, cantidad_neuronas)] for i in range(0, cantidad_neuronas)]
    for i in range(cantidad_neuronas):
        for j in range(cantidad_neuronas):
            pesos[i][j] = list(nuevo_conjunto[obtener_random(nuevo_conjunto)])
    return pesos

def obtener_distancias_por_un_punto(punto, pesos):
    distancias = np.zeros((len(pesos), len(pesos)))
    for i, fila_distancias in enumerate(pesos):
        for j, neurona in enumerate(fila_distancias):            
            distancias[i,j] = obtener_distancias(punto, [neurona])[0]    
    return distancias    

def obtener_neurona_ganadora(distancias):
    valor_minimo = 999
    indices = []
    for i in range(len(distancias)):
        for j in range(len(distancias)):
            if(distancias[i,j] < valor_minimo):
                valor_minimo = distancias[i,j]
                indices=[i,j]
    return indices

def actualizar_peso_neurona(neurona, X, eta, V=1):
    delta_w = V * eta * (X[:-1] - neurona)
    return neurona + delta_w

def actualizar_pesos_neuronas_vecinas(pesos, X, indice_neurona_ganadora, eta, R):
    i_ganadora, j_ganadora = indice_neurona_ganadora
    distancia_entre_neuronas_y_la_ganadora = obtener_distancias_por_un_punto(pesos[i_ganadora][j_ganadora], pesos)
    for i in range(len(distancia_entre_neuronas_y_la_ganadora)):
        for j in range(len(distancia_entre_neuronas_y_la_ganadora)):
            distancia_a_ganadora = distancia_entre_neuronas_y_la_ganadora[i][j]
            if(R > distancia_a_ganadora and [i,j] != indice_neurona_ganadora):
                V = e**((-2*distancia_a_ganadora)/R)
                pesos[i][j] = list(actualizar_peso_neurona(pesos[i][j], X, eta, V))
    return pesos