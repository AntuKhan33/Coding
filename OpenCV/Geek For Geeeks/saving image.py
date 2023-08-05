import cv2 as cv
import os

image_path=r"C:\Users\HP\Desktop\dist\OpenCV\Freecodecamp\Geek For Geeeks\Photos\cat.jpg"
directory=r"C:\Users\HP\Desktop\dist\OpenCV\Freecodecamp\Geek For Geeeks"
img=cv.imread(image_path)
os.chdir(directory)

print("before saving directory")
print(os.listdir(directory))
filename = 'savedImage.jpg'
x=input("please enter your desired name to save")

cv.imwrite(x +".jpg",img)
print("After saving image:")  
print(os.listdir(directory))
print('Successfully saved')