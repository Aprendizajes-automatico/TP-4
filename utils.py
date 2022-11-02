import numpy as np

def obtener_conjuntos_de_datos(conjunto):
    p80 = len(conjunto) * 0.80
    p20 = len(conjunto) * 0.20
    return conjunto[:int(p80)], conjunto[-int(p20):]

def flattenList(list):
    return [item for sublist in list for item in sublist]

def clasificar_imagen(conjunto, clase):
    nuevo_conjunto = np.empty((len(conjunto), 4))
    for i in range(len(conjunto)):
        for j in range(4):
            if(j == 3):
                nuevo_conjunto[i,j] = clase
            else:
                nuevo_conjunto[i,j] = conjunto[i,j]
    return nuevo_conjunto

def obtener_y_de_imagen(cantidad, clase):
    return [clase for i in range(cantidad)]