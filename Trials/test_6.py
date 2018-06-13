import face_recognition
import tkinter
arr= ['amit','ashok','pp','rakesh','shubham','mahipal','aman']
aman = face_recognition.load_image_file('aman.jpg')
amit = face_recognition.load_image_file('amit.png')
ashok = face_recognition.load_image_file('ashok.jpg')
pp= face_recognition.load_image_file('pp.png')
rakesh= face_recognition.load_image_file('rakesh1.jpeg')
shubham = face_recognition.load_image_file('shubham.jpg')
mahipal = face_recognition.load_image_file('mahipal.jpg')
face_enco=[amit,ashok,pp,rakesh,shubham,mahipal,aman]
image =  face_recognition.load_image_file('3.jpg')
im_enco = face_recognition.face_encodings(image)
ne_arr = []
for i in range(len(face_enco)):
    for j in range(len(im_enco)):
        pic = face_recognition.face_encodings(face_enco[i])
        check= face_recognition.compare_faces([im_enco[j]],pic[0],tolerance=0.55)
        if check == [True]:
            ne_arr.append(arr[i])
            print(ne_arr)
print(ne_arr)
