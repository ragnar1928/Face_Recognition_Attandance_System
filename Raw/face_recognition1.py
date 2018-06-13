import cv2
import numpy as np
from tkinter import *
import sys

video = cv2.VideoCapture(0)

while True:
    ret,cap=video.read()
    gray = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)
    cv2.imshow('livestream',gray)
    if cv2.waitKey(1) & 0xFF == ord('r'):
        file = "/home/aman-py/Desktop/Face_recognition/hell.jpg"
        cv2.imwrite(file, cap)
        break
video.release()
cv2.destroyAllWindows()
del(video)

import face_recognition
image = face_recognition.load_image_file('/home/aman-py/Desktop/Face_recognition/aman.jpg')
un_image = face_recognition.load_image_file('/home/aman-py/Desktop/Face_recognition/hell.jpg')
face_location=face_recognition.face_locations(image)
face_location2=face_recognition.face_locations(un_image)
face_landmarks_list = face_recognition.face_landmarks(image)
k_en = face_recognition.face_encodings(image)
u_en = face_recognition.face_encodings(un_image)
if face_location2 == [] :
   root = Tk()
   text = Text(root)
   text.insert(INSERT, "betterluck next time")
   text.insert(END, "............")
   text.pack()
   root.mainloop()
   sys.exit()

check = face_recognition.compare_faces([k_en[0]],u_en[0])

if check == [True]:
   root = Tk()
   text = Text(root)
   text.insert(INSERT, "Verified.....")
   text.insert(END, "u are aman")
   text.pack()
   root.mainloop()
else:
   root = Tk()
   text = Text(root)
   text.insert(INSERT, "Verified.....")
   text.insert(END, "u are not aman")
   text.pack()
   root.mainloop()
