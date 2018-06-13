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
        file = "/home/aman-py/Desktop/Face_recognition/hell.jpg"
        cv2.imwrite(file, cap)
        break
video.release()
cv2.destroyAllWindows()
del(video)


import face_recognition
import tkinter
arr= {'amit':'Absent','ashok':'Absent','pp':'Absent','rakesh':'Absent','shubham':'Absent','mahipal':'Absent','aman':'Absent'}
aman = face_recognition.load_image_file('aman.jpg')
amit = face_recognition.load_image_file('amit.png')
ashok = face_recognition.load_image_file('ashok.jpg')
pp= face_recognition.load_image_file('pp.png')
rakesh= face_recognition.load_image_file('rakesh1.jpeg')
shubham = face_recognition.load_image_file('shubham.jpg')
mahipal = face_recognition.load_image_file('mahipal.jpg')
face_enco=[amit,ashok,pp,rakesh,shubham,mahipal,aman]
image =  face_recognition.load_image_file('hell.jpg')
im_enco = face_recognition.face_encodings(image)
ne_arr = []
for i in range(len(face_enco)):
    for j in range(len(im_enco)):
        pic = face_recognition.face_encodings(face_enco[i])
        check= face_recognition.compare_faces([im_enco[j]],pic[0],tolerance=0.57)
        if check == [True]:
            arr[i]='Present'
root = Tk()
text = Text(root)
text.insert(INSERT, arr)
text.insert(END, "Have a good day")
text.pack()
root.mainloop()
