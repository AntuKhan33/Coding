import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import tensorflow as tf
from PIL import Image

from sklearn.model_selection import train_test_split

from tensorflow.keras.utils import normalize, to_categorical
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense 
image_directory='datasets/'
 
no_tumor_images=os.listdir(image_directory+"no")    
print(no_tumor_images)

path="no0.jpg"

print(path.split(".")[1])  


for i,image_name in enumerate(no_tumor_images):
    if (image_name.split(".")[1]=="jpg"):
        image=cv2.imread(image_directory+"/no"+image_name)
        image=Image.fromarray(image,"RGB")