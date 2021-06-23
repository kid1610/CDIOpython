import numpy as np
import os
import pickle, sqlite3
import cv2
from PIL import Image
#--------------------------------------------------------------------
# CODE KET NOI DU LIEU NHAN DIEN HINH ANH KHUON MAT
#Su dung thu vien(Mac dinh trong opencv)
#DEFAULT _ Face


#Ham lay id da dc luu o Sql Little
def getProfile(Id):
    conn=sqlite3.connect("FaceBase.db")
    query="SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(query)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile


def Face_detect():
    face_cascade = cv2.CascadeClassifier('khuon_mat.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Doc File
    recognizer.read("huanluyen/huanluyen.yml")
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_COMPLEX
    while True:
        #Load anh tu camera
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            nbr_predicted, conf = recognizer.predict(gray[y:y+h, x:x+w])
            if conf < 70:
                profile=getProfile(nbr_predicted)
                if profile != None:
                    cv2.putText(img, ""+str(profile[1]), (x+10, y), font, 1, (0,255,0), 1);

            else:
                cv2.putText(img, "Unknown", (x, y + h + 30), font, 0.4, (0, 0, 255), 1);


        cv2.imshow('img', img)
        if(cv2.waitKey(1) == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()

