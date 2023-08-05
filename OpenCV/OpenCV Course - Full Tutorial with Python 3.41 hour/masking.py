import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)


mask = cv.circle( blank,(img.shape[1]//2 ,img.shape[0]//2), 100, 255, -1)
cv.imshow("mask",mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("Masked Image",masked)


circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Weird Shape', weird_shape)

#basic Shape numpy
print("image shape",img.shape)
print("Blank shape",blank.shape)


print("image shape [0]//2:",img.shape[0]//2)
print("image shape [1]//2:",img.shape[1]//2 )


print(img.shape[1]//2 ,img.shape[0]//2)
print("image shape :2",img.shape[:2])


cv.waitKey(0)