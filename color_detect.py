import cv2
import numpy as np 
import pandas as pd 
import argparse
#creating argument parser to image path
ap=argparse.ArgumentParser()
imgName = "images.jpg"
 
image= cv2.imread(imgName)
cv2.imshow('MyImage', image)
#to detect red,blue,yellow,grey
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128]),
	([10, 100, 20], [25, 255, 255]),
        ([36, 25, 25], [70, 255,255])
]
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
