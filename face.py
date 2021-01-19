import cv2
import dlib
import sys
import numpy as np

scaler = 1
#Initialize face detector and shape predictor
detector = dlib.get_frontal_face_detector()
#load video
cap = cv2.VideoCapture(0)

while True:
    # read frame buffer from video
    ret, img = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        continue

    # resize frame
    img = cv2.resize(img, (int(img.shape[1] * scaler), int(img.shape[0] * scaler)))
    ori = img.copy()

    # detect faces
    faces = detector(img)

    #例外処理　顔が検出されなかった時
    if len(faces) == 0:
        print('no faces')
        img_rec = img

    for face in faces:
        # rectangle visualize
        img_rec = cv2.rectangle(img, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()),
                            color=(255, 255, 255), lineType=cv2.LINE_AA, thickness=2)

    # cv2.imshow('original', ori)
    cv2.imshow('img_rec', img_rec)

    if cv2.waitKey(1) == ord('q'):
        sys.exit(1)
