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

cv2.createTrackbar('Gamma','Trackbars',1,10,nothing) 

 

# Reading image
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\ImgP.bmp", cv2.IMREAD_COLOR)
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img1 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
h,w,c = img1.shape

c = 255/(np.log(1 + np.max(img1)))
log_transformed = c * np.log(1 + img1)
  
# Specify the data type.
log_transformed = np.array(log_transformed, dtype = np.uint8)

cv2.imshow("Frame",log_transformed)
cv2.moveWindow("Frame", 0, 0)

while True:
    gamma=cv2.getTrackbarPos('Gamma','Trackbars')
    # Apply gamma correction.
    gamma_corrected = np.array(255*(img1 / 255) ** (gamma/10), dtype = 'uint8')
    cv2.imshow("F",gamma_corrected)
  
    # De-allocate any associated memory usage 
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()