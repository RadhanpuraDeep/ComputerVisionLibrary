#kernel size is basically the number of rows and number of columns

import cv2 as cv 


img = cv.imread('E:/Computer Vision/image2.jpg')

resized = cv.resize(img, (500,500))
cv.imshow("Resized", resized)

#AVERAGING
average = cv.blur(resized, (7,7))
cv.imshow("Averrage", average)

#GAUSSIANBLUR

gauss = cv.GaussianBlur(resized, (7,7), 0)
cv.imshow("Gaussian Blur", gauss)

#MEDIANBLUR

median = cv.medianBlur(resized, 7)
cv.imshow("Median Blur", median)

#BILATERALBLUR

bilateral = cv.bilateralFilter(resized, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)