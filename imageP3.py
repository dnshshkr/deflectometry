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

cv2.createTrackbar('BlockSize','Trackbars',199,255,nothing) 
cv2.createTrackbar('Constant','Trackbars',5,100,nothing) 
 
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

    b=cv2.getTrackbarPos('BlockSize','Trackbars')
    c=cv2.getTrackbarPos('Constant','Trackbars')

    # applying different thresholding 
    # techniques on the input image
    try:
        thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                                cv2.THRESH_BINARY, b, c)
        
        thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY, b, c)
    except:
        pass
    
    # the window showing output images
    # with the corresponding thresholding 
    # techniques applied to the input image
    cv2.imshow('Adaptive Mean', thresh1)
    cv2.moveWindow("Adaptive Mean",400,0)
    cv2.imshow('Adaptive Gaussian', thresh2)
    cv2.moveWindow("Adaptive Gaussian",400+w,0)
    
    # De-allocate any associated memory usage 
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()