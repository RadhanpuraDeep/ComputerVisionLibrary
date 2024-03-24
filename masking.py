import cv2 as cv
import numpy as np 

img = cv.imread('E:/Computer Vision/image2.jpg')

resized = cv.resize(img, (500,500))
cv.imshow("resized", resized)

blank = np.zeros(resized.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

mask = cv.rectangle(blank, (resized.shape[1]//2, resized.shape[0]//2),(resized.shape[1]//2+100, resized.shape[0]//2+100), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(resized, resized, mask=mask)
cv.imshow("masked", masked)
cv.waitKey(0)