import cv2 as cv
import numpy as np

img = cv.imread('E:/Computer Vision/image1.jpg')

resized = cv.resize(img, (500,500))
cv.imshow('resized', resized)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobelx', sobelx)
cv.imshow('Sobely', sobely)
cv.imshow('Combined_Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)

cv.waitKey(0)