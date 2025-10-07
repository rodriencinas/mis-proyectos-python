#Opencv es usado para capturar video, porque el video no es más que la sucesión rápida de imágenes, de 'FRAMES'
import cv2, time

video = cv2.VideoCapture(0)

count_frames = 1

while True:
    count_frames += 1
    #lanzamos la cámara, esta función nos devuelve dos cosas, check = estado del encendido, frame=el nparray de la imagen capturada
    check, frame = video.read()

    print(check)
    print(frame)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Window", frame)
    cv2.imshow("Window2", gray_frame)
    #time.sleep(1)

    #capturamos la tecla que presionamos del teclado, cv2.waitKey() devuelve el código ASCII
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

print(count_frames)
cv2.destroyAllWindows()
video.release()