import imutils
import cv2

image = cv2.imread('imagem.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Tons de Cinza", gray)
cv2.waitKey(0)

blur = cv2.blur(gray, (5,5))
cv2.imshow("Filtro Blur", blur)
cv2.waitKey(0)

thresh = cv2.threshold(blur, 110, 250, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Binarizacao", thresh)
cv2.waitKey(0)

contornos = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
contornos = imutils.grab_contours(contornos)
output = image.copy()

for c in contornos:
    cv2.drawContours(output, [c], -1, (85, 200, 100), 3)

text = "{} objetos!".format(len(contornos))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(85, 200, 100), 2)
cv2.imshow("Trabalho final", output)
cv2.waitKey(0)