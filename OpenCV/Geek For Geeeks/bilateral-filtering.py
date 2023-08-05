import cv2

img=cv2.imread("lady.jpg")

# bilateral=cv2.bilateralFilter(img,75,75,75)
# bilateral1=cv2.bilateralFilter(img,0,75,75)
# bilateral2=cv2.bilateralFilter(img,75,0,75)
# bilateral3=cv2.bilateralFilter(img,75,75,0)

# cv2.imshow("picture",bilateral)
# cv2.imshow("picture",bilateral1)
# cv2.imshow("picture",bilateral2)
# cv2.imshow("picture",bilateral3)

cv2.waitKey(0)