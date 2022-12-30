# Python program to illustrate
# simple thresholding type on an image
     
# organizing imports
import cv2
import numpy as np

def nothing(x):
    pass


cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',0,0)
cv2.resizeWindow("Trackbars",400,300)

cv2.createTrackbar('Threshold','Trackbars',50,255,nothing) 
cv2.createTrackbar('Threshold MAX','Trackbars',255,255,nothing) 
 
# path to input image is specified and 
# image is loaded with imread command
img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\ImgP.bmp")
scale_percent = 10 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
image1 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
h,w,c = image1.shape
 
# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
 
# applying different thresholding
# techniques on the input image
# all pixels value above 120 will
# be set to 255
while True:

    t=cv2.getTrackbarPos('Threshold','Trackbars')
    t2=cv2.getTrackbarPos('Threshold MAX','Trackbars')

    ret, thresh1 = cv2.threshold(img, t, t2, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, t, t2, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, t, t2, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, t, t2, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, t, t2, cv2.THRESH_TOZERO_INV)
    
    # the window showing output images
    # with the corresponding thresholding
    # techniques applied to the input images
    cv2.imshow('Binary Threshold', thresh1)
    cv2.moveWindow("Binary Threshold",0,0)
    cv2.imshow('Binary Threshold Inverted', thresh2)
    cv2.moveWindow("Binary Threshold Inverted",w,0)
    cv2.imshow('Truncated Threshold', thresh3)
    cv2.moveWindow("Truncated Threshold",2*w,0)
    cv2.imshow('Set to 0', thresh4)
    cv2.moveWindow("Set to 0",0,h)
    cv2.imshow('Set to 0 Inverted', thresh5)
    cv2.moveWindow("Set to 0 Inverted",w,h)
    cv2.imshow('ORI', img)
    cv2.moveWindow("ORI",2*w,h)
    
    # De-allocate any associated memory usage 
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()