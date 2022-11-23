import cv2
from PIL import ImageFilter, Image
import numpy
import matplotlib.pyplot as plt

image = cv2.imread('templates\\1.jfif')
cv2.imshow('Original',image)
print(image.size)
color = image[150, 150]
print(color)
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', grayscale)
im = Image.fromarray(grayscale)
im1 = im.filter(ImageFilter.GaussianBlur(radius = 3))
# cv2.imshow('Blur', im1.)
opencvImage = cv2.cvtColor(numpy.array(im1), cv2.COLOR_RGB2BGR)
# im1.show(opencvImage)
cv2.imshow("Blur", opencvImage)


# Reshaping the image into a 2D array of pixels and 3 color values (RGB)
pixel_vals = opencvImage.reshape((-1,3))
 
# Convert to float type
pixel_vals = numpy.float32(pixel_vals)


#the below line of code defines the criteria for the algorithm to stop running,
#which will happen is 100 iterations are run or the epsilon (which is the required accuracy)
#becomes 85%
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
 
# then perform k-means clustering with number of clusters defined as 3
#also random centres are initially choosed for k-means clustering
k = 1
retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
 
# convert data into 8-bit values
centers = numpy.uint8(centers)
segmented_data = centers[labels.flatten()]
 
# reshape data into the original image dimensions
segmented_image = segmented_data.reshape((image.shape))
 
# cv2.imshow("Op", segmented_image)
plt.imshow(segmented_image)
plt.waitforbuttonpress()
cv2.waitKey(0)