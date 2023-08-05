import cv2 as cv

image =cv.imread("Photos\cat.jpg")

# cv.imshow("Cat",image)
h,w=image.shape[:2]

print("heigth {} ,width {}".format(h,w))

# cv.waitKey(0)
# cv.destroyAllWindows()

(B, G, R) = image[400, 100]
  
# Displaying the pixel values
print("R = {}, G = {}, B = {}".format(R, G, B))
  
# We can also pass the channel to extract 
# the value for a specific channel
B = image[100, 100, 0]
print("B = {}".format(B))

# roi=image[100:500,200:700]
# cv.imshow("Cat",roi)
ratio=800/w
dim=(800,int(h*ratio))


# resize = cv.resize(image, (800, 800))
# cv.imshow("Cat_Resized",resize)
# center=(w//2,h//2)
# print(center)

# matrix=cv.getRotationMatrix2D(center,-45,1.0)

# rotated=cv.warpAffine(image,matrix,(w,h))
# cv.imshow("rotated",rotated)

output=image.copy()
# rectangle=cv.rectangle(output,(150,90),(500,40),(255,0,0),2)
text=cv.putText(output,"HELLO",(150,90),cv.FONT_HERSHEY_COMPLEX,4,(0,0,255),2)

cv.imshow("rectangle_show",text)

# cv.imshow("rectangle_show",rectangle)



cv.waitKey(0)
cv.destroyAllWindows()

