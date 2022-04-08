#importar librerías
import cv2
import os
 
#crear variable de la ruta donde están las imágenes
path = r'./img'

#crear una array con el nombre de todos los archivos y carpetas
#dentro de pathww
lista = os.listdir(path)

#iterar la lista
for i in lista:
    #concatena la ruta + nombre de la imagen
    img = cv2.imread(path+"\\"+i)
    #imagen de 64 px x 64 px
    dimensiones = (64, 64)
    #recorte de la imágen
    img = img[60:1000, 430:1370]
    #reescala la imagen recortada
    resized = cv2.resize(img, dimensiones)
    #reescribe la imagen recortada y escalada por la original
    cv2.imwrite(path+"\\"+i, resized)