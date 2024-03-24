import cv2 as cv
import numpy as np

img = cv.imread('E:/Computer Vision/image2.jpg')

resized = cv.resize(img, (500,500))
cv.imshow("Resized", resized)

blank = np.zeros(resized.shape[:2], dtype='uint8')

b,g,r = cv.split(resized)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)