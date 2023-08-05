import cv2 as cv

image=cv.imread("zahid.jpg",0)
cv.imshow("orginal photo",image)
cv.waitKey(0)

# gray_image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# cv.imshow("grayscale",gray_image)

cv.waitKey(0)
cv.destroyAllWindows()