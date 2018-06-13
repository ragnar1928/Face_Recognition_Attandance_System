import cv2
import numpy as np
from tkinter import *
import sys

video = cv2.VideoCapture(0)

while True:
    ret,cap=video.read()
    gray = cv2.cvtColor(cap,0)
    cv2.imshow('livestream',gray)
    if cv2.waitKey(1) & 0xFF == ord('r'):
        file = "/home/aman-py/Desktop/Face_recognition/Final/hell.jpg"
        cv2.imwrite(file, cap)
        break
video.release()
cv2.destroyAllWindows()
del(video)

import face_recognition
from tkinter import *
import pandas as pd
arr = {'Students':['Amit','Ashok','PP','Rakesh','Shubham','Mahipal','Aman'],'Attandace':['Absent','Absent','Absent','Absent','Absent','Absent','Absent'],'Branch':['CS','CS','CS','CS','CS','CS','CS'],'Course':['B.tech','B.tech','B.tech','B.tech','B.tech','B.tech','B.tech']}
face=['Amit','Ashok','PP','Rakesh','Shubham','Mahipal','Aman']
aman = face_recognition.load_image_file('Aman.png')
amit = face_recognition.load_image_file('Amit.png')
ashok = face_recognition.load_image_file('Ashok.png')
pp= face_recognition.load_image_file('PP.png')
rakesh= face_recognition.load_image_file('Rakesh.png')
shubham = face_recognition.load_image_file('Shubham.png')
mahipal = face_recognition.load_image_file('Mahipal.png')
face_enco=[amit,ashok,pp,rakesh,shubham,mahipal,aman]
image =  face_recognition.load_image_file('hell.jpg')
im_enco = face_recognition.face_encodings(image)
for i in range(len(face_enco)):
    for j in range(len(im_enco)):
        pic = face_recognition.face_encodings(face_enco[i])
        check= face_recognition.compare_faces([im_enco[j]],pic[0],tolerance=0.55)
        if check == [True]:
            arr['Attandace'][i]='Present'
data = pd.DataFrame(arr,index=range(1,8))
root = Tk()
root.title('Attandance Sheet')
text = Text(root)
text.insert(INSERT, data)
text.insert(END, "\nHave a good day")
text.pack()
root.mainloop()
