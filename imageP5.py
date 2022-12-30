# Python code to find the co-ordinates of
# the contours detected in an image.
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Reading image
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\ImgP.bmp", cv2.IMREAD_COLOR)
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img2 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
h,w,c = img2.shape
# Reading same image in another 
# variable and converting to gray scale.
img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\ImgP.bmp", cv2.IMREAD_GRAYSCALE)
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img1 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
h,w = img1.shape
# Converting image to a binary image
# ( black and white only image).
_, threshold = cv2.threshold(img1, 110, 255, cv2.THRESH_BINARY)
  
# Detecting contours in image.
contours, _= cv2.findContours(threshold, cv2.RETR_TREE,
                               cv2.CHAIN_APPROX_SIMPLE)
  
# Going through every contours found in the image.
for cnt in contours :
  
    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
  
    # draws boundary of contours.
    cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5) 
  
    # Used to flatted the array containing
    # the co-ordinates of the vertices.
    n = approx.ravel() 
    i = 0
  
    for j in n :
        if(i % 2 == 0):
            x = n[i]
            y = n[i + 1]
  
            # String containing the co-ordinates.
            string = str(x) + " " + str(y) 
  
            if(i == 0):
                # text on topmost co-ordinate.
                cv2.putText(img2, "Arrow tip", (x, y),
                                font, 0.5, (255, 0, 0)) 
            else:
                # text on remaining co-ordinates.
                cv2.putText(img2, string, (x, y), 
                          font, 0.5, (0, 255, 0)) 
        i = i + 1
  
# Showing the final image.
cv2.imshow('image2', img2) 
cv2.moveWindow("image2",0,0)

# find frequency of pixels in range 0-255
histr = cv2.calcHist([img1],[0],None,[256],[0,256])
  
# show the plotting graph of an image
plt.plot(histr)
plt.show()

# Taking a matrix of size 5 as the kernel
kernel = np.ones((5, 5), np.uint8)
 
# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
img_erosion = cv2.erode(img1, kernel, iterations=1)
img_dilation = cv2.dilate(img1, kernel, iterations=1)
 
cv2.imshow('Input', img1)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)
  
# Exiting the window if 'q' is pressed on the keyboard.
if cv2.waitKey(0) & 0xFF == ord('q'): 
    cv2.destroyAllWindows()