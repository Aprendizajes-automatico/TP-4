import numpy as np
import matplotlib.pyplot as plt
import random

def trazar_linea():
    plt.plot([0,5], [2,7])

def formula_y(x):
    return x + 2

def obtener_puntos():
    puntos = np.empty((20,3))
    for i in range(20):
        for j in range(3):
            if(j == 2):
                x1 = puntos[i,0]
                x2 = puntos[i,1]
                puntos[i,j] = 1 if x2 <= formula_y(x1) else -1
            else:
                puntos[i,j] = random.uniform(0, 5)
    return puntos

def mostrar_puntos_en_plano(puntos):
    #Conjuntos de x
    X = puntos[:,[0,1]]
    #Columna de Y
    y = puntos[:,-1]
    # Plot de todos los Xi con Y = -1
    plt.plot(X[:, 0][y == -1], X[:, 1][y == -1], 'r^')
    # Plot de todos los Xi con Y = 1
    plt.plot(X[:, 0][y == 1], X[:, 1][y == 1], 'bs')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def perceptron(puntos):
    pesos = np.array([
        [0], 
        [0], 
    ])
    entradas = puntos[:,[0,1]]
    #Columna de Y
    y = puntos[:,-1]
    salidas = np.array([[int(punto)] for punto in y])
    tasa_de_aprendizaje = 0.1
    error = 1
    i = 0
    cota = 1000
    while(error > 0 & i < cota):
        print(salidas)
        exitacion = np.dot(entradas[i], pesos) #Multiplicaciones de w1*x1+w2*x2
        activacion = signo(exitacion)
        error = calcular_error(salidas[i], activacion) #Error cometido, (Aprendizaje supervisado)
        ajuste = tasa_de_aprendizaje*error #Ajustar el error en base a la tasa de aprendizaje 
        pesos = ajustar_pesos(entradas[i], pesos, ajuste[0]) #Actualiza los nuevos valores de los pesos ajustados
        i+=1
    return pesos

def signo(exitacion):
    return 1 if (exitacion >= 0) else 0	

def calcular_error(salida, activacion):
	return salida-activacion

def ajustar_pesos(entradas, pesos, ajuste):
	suma_entradas_ajuste = np.array([entradas*ajuste]).T
	return np.add(pesos, suma_entradas_ajuste)#Actualiza los pesos, sumandole el ajuste
