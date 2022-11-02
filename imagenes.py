import cv2
import random

from utils import flattenList, obtener_conjuntos_de_datos, obtener_y_de_imagen

def obtener_conjuntos(con_valores_random=True):

    conjuntos_training_X = []
    conjuntos_training_Y = []
    conjuntos_test_X = []
    conjuntos_test_Y = []
    for i, image in enumerate(["cielo.jpg", "pasto.jpg", "vaca.jpg"]):
        # Esto devuelve una lista de lista matrices, que representa 
        # El tamaño representa la cantidad de listas por la altura de la foto
        # len(img) -> 165 Es la cantidad de px de altura.
        # Dentro de cada elemento hay una lista de matrices que representan el px a lo ancho
        # len(img[0]) -> 215
        img = cv2.imread("imagenes/" + image, cv2.IMREAD_COLOR)
        img = random.choices(img, k=100) if con_valores_random else img
        # Se le pone img[0] porque devuelve una tupla (val, dtype)
        img = [tupla[0] for tupla in img]
        # Divide el conjunto en entrenamiento y test
        training_imagen, test_imagen = obtener_conjuntos_de_datos(img)
        # Punto 2. a
        # Valores Y de las imagenes. Clase 0 -> [0,0,0,0,0,0..0]
        training_Y = obtener_y_de_imagen(len(training_imagen), i)
        test_Y = obtener_y_de_imagen(len(test_imagen), i)
        
        conjuntos_training_X.append(training_imagen)
        conjuntos_test_X.append(test_imagen)
        conjuntos_training_Y.append(training_Y)
        conjuntos_test_Y.append(test_Y)
        #Flatteo las listas así tengo todos los valores en una lista sola
        #[[1,2,3], [4,5,6]] -> [1,2,3,4,5,6]
        if(i == 2):
            conjuntos_training_X = flattenList(conjuntos_training_X)
            conjuntos_training_Y = flattenList(conjuntos_training_Y)
            conjuntos_test_X = flattenList(conjuntos_test_X)
            conjuntos_test_Y = flattenList(conjuntos_test_Y)
    
    return conjuntos_training_X, conjuntos_training_Y, conjuntos_test_X, conjuntos_test_Y