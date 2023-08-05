import cv2 as cv

img=cv.imread("Photos\cat.jpg")
cv.imshow("view",img)

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("photo",gray)


blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)


# median=cv.medianBlur(img,3)
# cv.imshow("Median Blur",median)

canny=cv.Canny(img,125,125)
cv.imshow("Canny",canny)




canny1=cv.Canny(blur,125,125)
cv.imshow("Canny1",canny1)

dilated=cv.dilate(canny,(3,3),iterations=3)
cv.imshow("dilated",dilated)

eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow("Eroded",eroded)


resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",resized)


cropped=img[50:200,200:500]
cv.imshow("Cropped",cropped)


cv.waitKey(0)