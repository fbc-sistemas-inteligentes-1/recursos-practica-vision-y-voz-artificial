import cv2

imagen1=cv2.imread("originales/inner_square_6.jpg")
imagen2=cv2.imread("recortes/inner_square_6.jpg")
imagen1 = cv2.resize(imagen1, (300, 300))
imagen2 = cv2.resize(imagen2, (300, 300))
diferencias=cv2.absdiff(imagen1,imagen2)

imagenGris=cv2.cvtColor(diferencias,cv2.COLOR_BGR2GRAY)
contornos,c=cv2.findContours(imagenGris,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for contornoActual in contornos:
    if cv2.contourArea(contornoActual):
        x,y,ancho,alto=cv2.boundingRect(contornoActual)
        cv2.rectangle(imagen1,(x,y),(x+ancho,y+alto),(0,0,255),2)

while True:
    cv2.imshow("imagen1", imagen1)
    cv2.imshow("imagen2", imagen2)
    cv2.imshow("diferencia", diferencias)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
cv2.destroyAllWindows()