import cv2 
import numpy as np 
   
# path to input image is specified and  
# image is loaded with imread command 
img = cv2.imread('lady.jpg',0)

thresh1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,199,5) 
thresh2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,199,5)
cv2.imshow("Adaptive Mean",thresh1)
cv2.imshow("Adaptive Gausssain",thresh2)
cv2.waitKey(0)
 