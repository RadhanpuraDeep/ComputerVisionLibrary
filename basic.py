import cv2 as cv
img = cv.imread('E:/Computer Vision/image2.jpg')

cv.imshow('Me', img)

resized = cv.resize(img, (500,500))
cv.imshow("Resized", resized)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(resized, (3,3), cv.BORDER_DEFAULT)
cv.imshow('BLUR', blur)

canny = cv.Canny(blur, 125, 125)
cv.imshow('Canny Edge', canny)

dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

eroded = cv.erode(dilated, (3,3), iterations=4)
cv.imshow('Eroded', eroded)

cropped = resized[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)