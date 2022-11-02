import cv2
from imagenes import obtener_conjuntos
from r2 import mostrar_puntos_en_plano, obtener_puntos, perceptron, trazar_linea
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
import numpy as np


trazar_linea()
puntos = obtener_puntos()
#mostrar_puntos_en_plano(puntos)

print("-------------------")
print("Punto 2")
conjuntos_training_X_Random, conjuntos_training_Y_Random, conjuntos_test_X_Random, conjuntos_test_Y_Random = obtener_conjuntos()
print("Con valores Random")
#Probar distintos nucleos de C y kernel
clf = svm.SVC(C=100)
clf.fit(conjuntos_training_X_Random, conjuntos_training_Y_Random)
pred_conjunto_test_entero = clf.predict(conjuntos_test_X_Random)

print(confusion_matrix(conjuntos_test_Y_Random, pred_conjunto_test_entero, labels=[0,1,2]))
print(f"Accuracy: {100*accuracy_score(conjuntos_test_Y_Random, pred_conjunto_test_entero)}%")
print(f"Precision: {100*precision_score(conjuntos_test_Y_Random, pred_conjunto_test_entero, average='micro')}%")

print("-------------------")

print("Valores foto entera")
conjuntos_training_X_Entero, conjuntos_training_Y_Entero, conjuntos_test_X_Entero, conjuntos_test_Y_Entero = obtener_conjuntos(con_valores_random=False)
pred_conjunto_test_entero = clf.predict(conjuntos_test_X_Entero)

print(confusion_matrix(conjuntos_test_Y_Entero, pred_conjunto_test_entero, labels=[0,1,2]))
print(f"Accuracy: {100*accuracy_score(conjuntos_test_Y_Entero, pred_conjunto_test_entero)}%")
print(f"Precision: {100*precision_score(conjuntos_test_Y_Entero, pred_conjunto_test_entero, average='micro')}%")
print("-------------------")

img = cv2.imread("imagenes/cow.jpg", cv2.IMREAD_COLOR)
colores = {0: [255, 0, 0], 1: [0, 255, 0], 2: [0, 0, 255]}

ancho_foto = len(img[0])
altura_foto = len(img)
nueva_vaca = np.zeros((altura_foto, ancho_foto, 3),np.uint8)

for i in range(altura_foto):
    for j in range(ancho_foto):
        prediccion = clf.predict([img[i][j]])
        nueva_vaca[i,j] = colores[prediccion[0]]

cv2.imwrite("nueva_vaca.png",nueva_vaca)
