import cv2
import numpy as np

img = cv2.imread('lady.jpg',0)

ret,thresh1=(cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + 
                                            cv2.THRESH_OTSU)  )
cv2.imshow("Otsu Threshold",thresh1)

cv2.waitKey(0)