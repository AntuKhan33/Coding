import streamlit as st
import cv2
import matplotlib.pyplot as plt
import numpy as np
import maze

st.title('Maze Solver')
uploaded_file = st.file_uploader("Choose an image", ["jpg","jpeg","png"]) #image uploader
st.write('Or')
use_default_image = st.checkbox('Use default maze')
if use_default_image:
    opencv_image = cv2.imread('maze.jpg')

elif uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)