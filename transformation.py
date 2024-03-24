import cv2 as cv
import numpy as np

img = cv.imread('E:/Computer Vision/image2.jpg')
cv.imshow('Image', img)


resized = cv.resize(img, (500,500))
cv.imshow("Resized", resized)

def translate(resized, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(resized, 100, 100)
cv.imshow('Translated', translated)


#-x --> left
#-y --> up
#x --> right
#y --> down

def rotate(resized, angle, rotPoint=None):
    (height, width) = resized.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(resized, rotMat, dimensions)

rotated = rotate(resized, -45)
cv.imshow("Rotated", rotated)


cv.waitKey(0)