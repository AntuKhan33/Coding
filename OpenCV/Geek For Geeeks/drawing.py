import cv2
img=cv2.imread("lady.jpg")

# image=cv2.line(img,(0,0),(250,250),(0,255,0),2)
#image=cv2.arrowedLine(img,(0,0),(250,250),(0,255,0),2)
center_coordinates = (120, 100)
  
axesLength = (100, 50)
  
angle = 0
  
startAngle = 0
  
endAngle = 360
   
# Red color in BGR
color = (0, 0, 255)
   
# Line thickness of 5 px
thickness = 2
   
# Using cv2.ellipse() method
# Draw a ellipse with red line borders of thickness of 5 px
# image = cv2.ellipse(img, center_coordinates, axesLength,
#            angle, startAngle, endAngle, color, thickness)

# image=cv2.circle(img,(120,50),20,(255,255,255),-2)

#image=cv2.rectangle(img,(0,0),(250,250),(0,255,0),2)
image=cv2.putText(img,("hello"),(250,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA,False)


cv2.imshow("Windows",image)

cv2.waitKey(0)