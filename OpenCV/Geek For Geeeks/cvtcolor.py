import cv2
import numpy as np

img = cv2.imread('lady.jpg')

colorchange=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("Image",colorchange)



cv2.waitKey(0)
