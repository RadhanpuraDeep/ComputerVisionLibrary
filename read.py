import cv2 as cv

#img = cv.imread('E:/Computer Vision/IMG_20180603_212852.jpg')
#cv.imshow('ME', img)

capture = cv.VideoCapture('E:/Computer Vision/01156.MTS')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()