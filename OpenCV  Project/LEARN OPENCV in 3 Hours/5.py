import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")



cv2.imshow("Image",img)
# cv2.imshow("Output",imgOutput)

cv2.waitKey(0)