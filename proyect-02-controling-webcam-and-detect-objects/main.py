import cv2, pandas
from datetime import datetime

#algunas variables
first_frame = None
status_list = [None,None]
times_record = []
df = pandas.DataFrame(columns=["Start","End"])

video = cv2.VideoCapture(0)

while True:

    check,frame = video.read()

    #ubicamos el punto donde no hay movimiento, lo representamos con una variable
    status = 0
    #convertimos los cuadros a escala de grises, luego un difuminado
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21,21), 0)
    
    #guardamos en una variable el primer cuadro cuando se lanza la cámara, que usaremos como "Backgroud" como fondo
    if first_frame is None:
        first_frame = gray_frame
        continue

    #en este punto hacemos la comparación entre el first_frame con el current frame que es frame actual
    #ambos están 'difuminados', tanto el first_frame como el gray_frame... esto nos devuelve otra imagen
    delta_frame = cv2.absdiff(first_frame, gray_frame)

    #en este punto ya tenemos los píxeles los valores de los píxeles que nos indicarán dónde hay movimiento
    #por lo que ahora debemos clasificar estos valores 
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] 

    #ahora lo que haremos será dilatar o difuminar un poco para aquellas zonas en las que en realidad no hay movimiento, pero se detecta como tal
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    #una vez que tenemos todos estos pasos, lo que haremos será definir los contornos de lo que se está detectando
    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue

        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
        #ubicamos cuando el programa detecta movimiento, y lo mostramos
        status = 1
    
    status_list.append(status)
    if status_list[-1] == 1 and status_list[-2] == 0:
        times_record.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times_record.append(datetime.now())
    

    #print(status)


    #código para mostrar lo que vamos haciendo, las diferentes vistas del proceso de detección de movimiento
    #cv2.imshow("First Frame", first_frame) #mostramos el primer cuadro captado
    #cv2.imshow("Delta Frame", delta_frame) #mostramos el resultado de calcular la diff entre first_frame y gray_frame, ambos difuminados
    #cv2.imshow("Frames", frame) #mostramos lo que capta la cámara en vivo
    #cv2.imshow("Gray frame", gray_frame) #mostramos la imagen captada por la cámara en gris y blureada
    #cv2.imshow("Threshold frame", thresh_frame)#mostramos la imagen con el threshold aplicado
    cv2.imshow("Final window", frame)

    #print(thresh_frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times_record.append(datetime.now())
        break

#agregamos los datos guardados en la lista de los registros de tiempo en un DataFrame
df1 = pandas.DataFrame({"Start":times_record[::2], "End":times_record[1::2]})
df = pandas.concat([df, df1], ignore_index=True)


print(status_list)
print(times_record)
print(df)

#con los datos recolectados por la aplicación creamos un archivo .csv
df.to_csv("Times.cvs")

video.release()
cv2.destroyAllWindows()