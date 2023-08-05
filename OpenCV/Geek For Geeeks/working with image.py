import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("Photos/cat.jpg")
# photos=cv.imshow("Image",img)

# print(img.shape)

#rgb_img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
img=cv.imread("Photos/cat.jpg",cv.IMREAD_GRAYSCALE)
photos=cv.imshow("Image",img)
# plt.imshow(img)
# plt.waitforbuttonpress()
# plt.close('all')
cv.waitKey(0)

