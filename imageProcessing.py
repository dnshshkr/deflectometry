import cv2
import numpy as np
import matplotlib as plt

img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\ImgP.bmp")
scale_percent = 10 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
imageori = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# Canny edge detection.
edges = cv2.Canny(imageori, 100, 200)

#imageori = cv2.imread("C:\\Users\\syami\\Downloads\se1.png")
h,w,c = imageori.shape


# Creating kernel
kernel = np.ones((5, 5), np.uint8)
# Using cv2.erode() method 
erode1 = cv2.erode(imageori, kernel) 
# Creating kernel
kernel2 = np.ones((6, 6), np.uint8)
# Using cv2.erode() method 
erode2 = cv2.erode(imageori, kernel2, cv2.BORDER_REFLECT) 



# Displaying the image 
cv2.imshow("ORI", imageori) 
cv2.moveWindow("ORI",0,0)
cv2.imshow("ERODE 1", erode1) 
cv2.moveWindow("ERODE 1",w,0)
cv2.imshow("ERODE 2", erode2) 
cv2.moveWindow("ERODE 2",2*w,0)
cv2.imshow("EDGE", edges) 
cv2.moveWindow("EDGE",0,h)

cv2.waitKey(0)