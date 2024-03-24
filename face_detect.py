import cv2 as cv

img = cv.imread('E:/Computer Vision/IMG_20180603_212852.jpg')

resized = cv.resize(img, (700,800))
#cv.imshow('Resized', resized)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print('Number of faces found = ', len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(resized, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    
cv.imshow('Detected Faces', resized)

cv.waitKey(0)