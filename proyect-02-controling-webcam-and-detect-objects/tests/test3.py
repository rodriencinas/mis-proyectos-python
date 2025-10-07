import cv2

#creamos el objeto "clasificador" para lo que queremos buscar, en este caso caras
face_cascade = cv2.CascadeClassifier("data/Files/haarcascade_frontalface_default.xml")

#cargamos la imagen para trabajar en conjunto con el objeto clasificador, y luego transformamos la img a una escala de grises
img = cv2.imread("../data/Files/photo.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces.ndim)
print(faces.shape)
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)

resized_img = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))


cv2.imshow("Window", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()