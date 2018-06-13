import face_recognition
from tkinter import *
import pandas as pd
arr = {'Students':['Amit','Ashok','PP','Rakesh','Shubham','Mahipal','Aman'],'Attandace':['Absent','Absent','Absent','Absent','Absent','Absent','Absent'],'Branch':['CS','CS','CS','CS','CS','CS','CS'],'Course':['B.tech','B.tech','B.tech','B.tech','B.tech','B.tech','B.tech']}
face=['Amit','Ashok','PP','Rakesh','Shubham','Mahipal','Aman']
aman = face_recognition.load_image_file('aman.jpg')
amit = face_recognition.load_image_file('amit.png')
ashok = face_recognition.load_image_file('ashok.jpg')
pp= face_recognition.load_image_file('pp.png')
rakesh= face_recognition.load_image_file('rakesh1.jpeg')
shubham = face_recognition.load_image_file('shubham.jpg')
mahipal = face_recognition.load_image_file('mahipal.jpg')
face_enco=[amit,ashok,pp,rakesh,shubham,mahipal,aman]
image =  face_recognition.load_image_file('class.jpg')
im_enco = face_recognition.face_encodings(image)
ne_arr = []
for i in range(len(face_enco)):
    for j in range(len(im_enco)):
        pic = face_recognition.face_encodings(face_enco[i])
        check= face_recognition.compare_faces([im_enco[j]],pic[0],tolerance=0.57)
        if check == [True]:
            arr['Attandace'][i]='Present'
data = pd.DataFrame(arr)
root = Tk()
root.title('Attandance Sheet')
text = Text(root)
text.insert(INSERT, data)
text.insert(END, "\nHave a good day")
text.pack()
root.mainloop()
