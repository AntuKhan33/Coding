import cv2 as cv
import numpy as np

img=cv.imread("Photos/cats.jpg")

kernel=np.ones((5,5),np.uint8)

img_erosionn=cv.erode(img,kernel,iterations=1)

img_dilate=cv.dilate(img,kernel,iterations=1)

cv.imshow("original",img)
cv.imshow("img_erosionn",img_erosionn)
cv.imshow("img_dilate",img_dilate)
cv.waitKey(0)