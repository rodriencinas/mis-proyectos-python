import cv2

faces_cascade = cv2.CascadeClassifier("../data/Files/haarcascade_frontalface_default.xml")

img = cv2.imread("../data/Files/news.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faces_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)

cv2.imshow("Window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#En este caso estaría detectando la cara de la mujer, pero NO la del hombre, de hecho así como está el código detecta la mano del hombre
#Deberíamos modificar un poco los valores de los argumentos del detector de faces
