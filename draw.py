import cv2 as cv 
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('Blank', blank)

#blank[200:300, 300:400] = 0,255,0
#cv.imshow("Green", blank)

#cv.rectangle(blank,(0,0), (250,500), (0,255,0), thickness=cv.FILLED)
#cv.imshow("Rectanle", blank)

#cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
#cv.imshow("Circle", blank)

#cv.line(blank, (250,250), 40, (255,255,255), thickness=3)
#cv.imshow("Line", blank)

cv.putText(blank, "Hello", (255,255), cv.FONT_HERSHEY_TRIPLEX,1.0, (0,255,0),2)
cv.imshow('Text', blank)
cv.waitKey(0)
