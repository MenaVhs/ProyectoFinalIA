import cv2

image = cv2.imread('./img/img1.png')

print('image.shape=', image.shape)

imageOut = image[60:1000, 430:1370]

cv2.imshow('Imagen de entrada', image)
cv2.imshow('Imagen de salida', imageOut)

cv2.waitKey(0)
cv2.destroyAllWindows()