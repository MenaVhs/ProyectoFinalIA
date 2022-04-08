import cv2
import os
 
path = r'./img'

lista = os.listdir(path)

for i in os.listdir(path):
    img = cv2.imread(path+"\\"+i)
    #valor = 2
    #width = int(img.shape[1]*valor)
    #height = int(img.shape[0]*valor)
    #dim = (width, height)
    dim = (64, 64)
    resized = cv2.resize(img, dim)
    cv2.imwrite(path+"\\"+i, resized)