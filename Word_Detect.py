import cv2
import pytesseract

# pytesseract .exe file location
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# add image to recognize 
img = cv2.imread('Images/1.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# detecting only numbers
hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_data(img)
for x,b in enumerate(boxes .splitlines()):
    if x!=0:
        b = b.split()
        if len(b)==12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,y+h),(0,255,0),3)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('Result', img)
cv2.waitKey(0)
