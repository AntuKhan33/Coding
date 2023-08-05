import cv2
import numpy as np

# Open the image.
img = cv2.imread('lady.jpg')
values=[0.1, 0.5, 1.2, 2.2]
# Trying 4 gamma values.
for gamma in values :
	
	# Apply gamma correction.
	gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')

	# Save edited images.
	cv2.imshow('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)
cv2.waitKey(0)
