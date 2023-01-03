import numpy as np
import matplotlib.pyplot as plt
import cv2

def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',0,0)
cv2.resizeWindow("Trackbars",640,300)

cv2.createTrackbar('Period','Trackbars',50,350,nothing) 
cv2.createTrackbar('X axis max','Trackbars',501,501,nothing) 
cv2.createTrackbar('X axis min','Trackbars',50,50,nothing) 
cv2.setTrackbarMin('X axis min', 'Trackbars', -500)
cv2.createTrackbar('Orientation','Trackbars',0,1,nothing) 

while True:

    wave=cv2.getTrackbarPos('Period','Trackbars',)
    sizeXmax=cv2.getTrackbarPos('X axis max','Trackbars')
    sizeXmin=cv2.getTrackbarPos('X axis min','Trackbars')
    orientation=cv2.getTrackbarPos('Orientation','Trackbars')
    if sizeXmax<=52:
        sizeXmax=52
    #x = np.arange(sizeXmin, sizeXmax, 1)
    x = np.arange(-250, 500, 1)
    X, Y = np.meshgrid(x, x)
    wavelength = wave
    
    if orientation:
        grating = np.sin(2 * np.pi * X / wavelength) 
    else:
        grating = np.sin(2 * np.pi * Y / wavelength)
    

    ret, grating2 = cv2.threshold(grating, 0, 0.5, cv2.THRESH_BINARY)
    cv2.namedWindow("Fringe", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Fringe",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.moveWindow("Fringe",1920,0)
    cv2.imshow("Fringe", grating2)
   

    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()

