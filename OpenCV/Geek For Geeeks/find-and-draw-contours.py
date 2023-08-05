import cv2
import numpy as np
image = cv2.imread('lady.jpg',0)
edged = cv2.Canny(image, 30, 200)
cv2.waitKey(0)

contours,hierarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

cv2.imshow("canny edged",edged)
cv2.waitKey(0)

print("NUmber of contours found",str(len(contours)))

cv2.drawContours(image,contours,-1,(0,244,0),3)

cv2.imshow("Contours",image)
cv2.waitKey(0)
cv2.destroyAllWindows()