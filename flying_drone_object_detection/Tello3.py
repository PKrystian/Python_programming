from djitellopy import Tello
import cv2
import os

def detect_face(image_source):
    face_detector = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml'))
    img = cv2.imread(image_source)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    amount_found = len(faces)

    if amount_found != 0:
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('img',img)
        cv2.waitKey(0)

tello = Tello()

tello.connect()
tello.takeoff()
tello.move_up(50)

for x in range (10):
    print(f"{x} rotation\n")
    tello.rotate_counter_clockwise(30)
    tello.streamon()
    frame_read = tello.get_frame_read()
    cv2.imwrite("picture.jpg", frame_read.frame)
    image_source = "picture.jpg"
    face_detector = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml'))
    img = cv2.imread(image_source)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    amount_found = len(faces)

    if amount_found != 0:
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('img',img)
        cv2.waitKey(0)

    if amount_found != 0:
        break

tello.move_back(50)
tello.land()