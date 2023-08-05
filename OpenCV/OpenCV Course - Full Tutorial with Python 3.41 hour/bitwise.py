import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("Rectangle",rectangle)
cv.imshow("circle",circle)

# print(rectangle.shape)
# print(circle.shape)

# bitwise=cv.bitwise_and(rectangle,circle)
# cv.imshow("bitwise",bitwise)


# bitwise=cv.bitwise_or(rectangle,circle)
# cv.imshow("bitwise",bitwise)


# bitwise_xor = cv.bitwise_xor(rectangle, circle)
# cv.imshow('Bitwise XOR', bitwise_xor)


bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Circle NOT', bitwise_not)



cv.waitKey(0)
