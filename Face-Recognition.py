import numpy as np
import cv2
import face_recognition
import os

path = 'ImagesAttendance'
images = []
classNames = []

myList = os.listdir(path)
print(myList)

# adding images from dir
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

# encoding them
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)
print('Encoding Complete !')

cap = cv2.VideoCapture(0)

while True:
    success , img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    facesInFrame  = face_recognition.face_locations(imgS)
    encodeInFrame = face_recognition.face_encodings(imgS,facesInFrame)

    for encodeface,faceLoc in zip (encodeInFrame,facesInFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeface)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeface)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4 ,x2*4 ,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

    cv2.imshow('Webcam',img)
    cv2.waitKey(1)