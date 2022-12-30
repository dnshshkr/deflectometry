# Python code to find the co-ordinates of
# the contours detected in an image.
import numpy as np
import cv2
from matplotlib import pyplot as plt

def nothing(x):
    pass


cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',0,0)
cv2.resizeWindow("Trackbars",400,300)

cv2.createTrackbar('r1','Trackbars',70,200,nothing) 
cv2.createTrackbar('s1','Trackbars',0,10,nothing) 
cv2.createTrackbar('r2','Trackbars',140,150,nothing) 
cv2.createTrackbar('s2','Trackbars',255,255,nothing) 

 

# Reading image
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\ImgP.bmp", cv2.IMREAD_COLOR)
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img1 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
h,w,c = img1.shape

# Function to map each intensity level to output intensity level.
def pixelVal(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1)*pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2
  
# Define parameters.
r1 = 70
s1 = 0
r2 = 140
s2 = 255
  
# Vectorize the function to apply it to each value in the Numpy array.
pixelVal_vec = np.vectorize(pixelVal)

while True:
    r1=cv2.getTrackbarPos('r1','Trackbars')
    s1=cv2.getTrackbarPos('s1','Trackbars')
    r2=cv2.getTrackbarPos('r2','Trackbars')
    s2=cv2.getTrackbarPos('s2','Trackbars')
# Apply contrast stretching.
    contrast_stretched = pixelVal_vec(img1, r1, s1, r2, s2)
    cv2.imshow("F",contrast_stretched)
        # De-allocate any associated memory usage 
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()