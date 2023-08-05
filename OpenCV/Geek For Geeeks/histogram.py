# importing required libraries of opencv
import cv2

# importing library for plotting
from matplotlib import pyplot as plt

# reads an input image
img = cv2.imread('Photos/cats.jpg',0)

# find frequency of pixels in range 0-255
# histr = cv2.calcHist([img],[0],None,[256],[0,256])
# plt.hist(img.ravel(),256,[0,256])

# show the plotting graph of an image
# plt.plot(histr)
# plt.show()

ret,thresh1=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,120,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
ret,thresh5=cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)
cv2.waitKey(0)