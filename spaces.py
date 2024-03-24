#OpenCV follows the order of BGR
#rest all follow the order of RGB
import cv2 as cv
import matplotlib.pyplot as plt



img = cv.imread('E:/Computer Vision/image2.jpg')

resized = cv.resize(img, (500,500))
cv.imshow("Resized", resized)

#plt.imshow(resized)
#plt.show()

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

hsv = cv.cvtColor(resized, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

lab = cv.cvtColor(resized, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

rgb = cv.cvtColor(resized, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("LAB-->BGR", lab_bgr)




plt.imshow(rgb)
plt.show()

cv.waitKey(0)