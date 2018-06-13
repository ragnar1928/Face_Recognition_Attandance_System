import cv2
import numpy as np
 
# Camera 0 is the integrated web cam on my netbook
camera_port = 0
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 60
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im
 
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
 temp = get_image()
print("Taking image...")
# Take the actual image we want to keep
camera_capture = get_image()
file = "/home/aman-py/Desktop/Face_recognition/test_image4.jpg"
# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
cv2.imwrite(file, camera_capture)
 
# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)

import face_recognition
image = face_recognition.load_image_file('aman.jpg',mode='RGB')
un_image = face_recognition.load_image_file('test_image4.jpg')
face_location=face_recognition.face_locations(image)
face_location2=face_recognition.face_locations(un_image)
print(face_location2)
face_landmarks_list = face_recognition.face_landmarks(image)
k_en = face_recognition.face_encodings(image)
u_en = face_recognition.face_encodings(un_image)
check = face_recognition.compare_faces([k_en[0]],u_en[0])
if check == True:
    print('Verified U are Aman')
else:
    print('U are Not Aman')
