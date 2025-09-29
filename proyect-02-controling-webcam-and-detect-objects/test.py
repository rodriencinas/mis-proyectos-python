import cv2

img = cv2.imread("data/galaxy.jpg", 0)

print(img.shape)
print(img.ndim)
print(type(img))
print(img)

#crearemos una imagen redimensionada de la imagen original
resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imwrite("data/new_reized_img.jpg", resized_img)
cv2.imshow("Window", resized_img) #show img
cv2.waitKey(0) #tiempo que mantendré la ventana llamada anteriormente
cv2.destroyAllWindows()