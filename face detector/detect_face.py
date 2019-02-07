import numpy as np
import cv2 as cv
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
#img = cv.imread('C:\\Users\\Josh\\Pictures\\Saved Pictures\\Josh_Suit.png')

cap = cv.VideoCapture(1)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    print(ret)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv.imshow('img',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
print('exited')
cap.release()
cv.destroyAllWindows()

