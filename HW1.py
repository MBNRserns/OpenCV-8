import cv2
import os



haar_file="C:/Users/mbnrs/OneDrive/Documents/Jetlearn/OpenCV-8/haarcascade_frontalface_default.xml"
datasets="C:/Users/mbnrs/OneDrive/Documents/Jetlearn/OpenCV-8/DataSets"
sub_data="Marco"
path = os.path.join(datasets, sub_data) 

if not os.path.isdir(path):
    os.mkdir(path)

# Defining the size of images
(width, height) = (130,100)


face_cascade = cv2.CascadeClassifier(haar_file)
#0 = webcam(inbuilt camera)
# 1 = external 
webcam=cv2.VideoCapture(1)

count = 1
while count <= 30:
    (ret, img) = webcam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #(image, ScaleFactor, Min Neighbours)
    faces = face_cascade.detectMultiScale(gray, 1.3,4)
    print(faces)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        face = gray[y:y +h, x:x + w]
        face_resize = cv2.resize(face, (width,height))
        cv2.imwrite("% s/% s.png" % (path, count), face_resize)
    count += 1

    cv2.imshow("OpenCV", img)
    key = cv2.waitKey(0)
    if key == 27:
        break
    

