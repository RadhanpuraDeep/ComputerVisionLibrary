import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread('E:/Computer Vision/image2.jpg')

resized = cv.resize(img, (500,500))
cv.imshow('Resized', resized)

blank = np.zeros(resized.shape[:2], dtype='uint8')

#gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

circle = cv.circle(blank, (resized.shape[1]//2, resized.shape[0]//2), 100, 255, -1)


mask = cv.bitwise_and(resized, resized, mask = circle)
cv.imshow('Mask', mask)

#gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

#plt.figure()
#plt.title('Grayscale Histogram')
#plt.xlabel('X-axis')
#plt.ylabel('Y-axis')
#plt.plot(gray_hist)
#plt.xlim([0,256])
#plt.show()

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([resized], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)