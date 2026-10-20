import math
import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np


cap = cv2.VideoCapture('Videos/vid (4).mp4')

mycolorFinder = ColorFinder(False)

hsvVals = {'hmin': 8, 'smin': 96, 'vmin': 115, 'hmax': 14, 'smax': 255, 'vmax': 255}

poslistX=[]
poslistY=[]

xlist=[ item for item in range(0,1300)]
prediction=False
while True:
    success,img=cap.read()
    # img=cv2.imread("Ball.png")
    
    img=img[0:900,:]
    
    
    imgColor,mask=mycolorFinder.update(img,hsvVals)
    
    imgContours,contours =cvzone.findContours(img,mask,minArea=500)
    
    
    
    
    if contours :
        poslistX.append(contours [0]['center'][0])
        poslistY.append(contours [0]['center'][1])
        
    if poslistX:
        
        
        A, B, C = np.polyfit(poslistX, poslistY, 2)

        for i,(posX,posY) in enumerate(zip(poslistX,poslistY)):
            pos=posX,posY
            # print("pos value is ",pos, " and pos[i-1] is ",poslist[i-1])
            cv2.circle(imgContours,pos,10,(0,255,0),cv2.FILLED,)
            if i==0:
                
                cv2.line(imgContours,pos,pos,(0,255,0),2)
            else:
                
                cv2.line(imgContours,pos,(poslistX[i-1],poslistY[i-1]),(0,255,0),2)
        
        for  x in xlist:
            y=int(A*x**2+B*x+C)
            cv2.circle(imgContours,(x,y),1,(255,0,0),cv2.FILLED)


        if len(poslistX)<10:
    #x-> 330-430 and y->590
            a=A
            b=B
            c=C-590
            
            x = int((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
            
        prediction=330<x<430
        print(prediction,x)
            
        if  prediction:
            
            cvzone.putTextRect(imgContours,"Basket Ball Shot",(50,150),scale=7,
                            thickness=5,colorR=(0,200,0),offset=20)
        else:
            cvzone.putTextRect(imgContours,"No Basket Ball Shot",(50,150),
                            colorR=(0,0,200),scale=7,thickness=5,offset=20)

    
    
    
    
    
    
    
    
    #img=cv2.resize(mask,(0,0),None,0.7,0.7)
    #imgColor=cv2.resize(imgColor,(0,0),None,0.7,0.7)

    imgContours=cv2.resize(imgContours,(0,0),None,0.7,0.7)
    #cv2.imshow("Image",img)
    cv2.imshow("Imagecolor",imgContours)
    cv2.waitKey(50)