import cv2
import numpy as np

filas=3
columnas=3

lienzo=np.zeros((filas,columnas,3),np.uint8)
print(lienzo)

#       B   G   R
rojo=[0,0,255]
azul=[255,0,0]
amarillo=[0,255,255]

lienzo[0,0]=amarillo
lienzo[0,1]=amarillo
lienzo[0,2]=amarillo

lienzo[1,0]=azul
lienzo[1,1]=azul
lienzo[1,2]=azul

lienzo[2,0]=rojo
lienzo[2,1]=rojo
lienzo[2,2]=rojo

cv2.imwrite("imagenes/bandera.png",lienzo)