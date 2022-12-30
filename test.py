import pygame
import math
import numpy as np
from pygame.locals import *
import cv2
 
# constants 
w = 1920
h = 1080 
    
# place fringes on the screen
def fringeGen(width, height, desired_period = 1, pixel_size = 440, calib = False, vert=True, phase=0):

    size = (width,height)
    rgb_img = np.zeros((w,h,3))

    # if we want a calibration screen
    if calib:
        img = np.ones((w,h))*(desired_period%255)

    else:
    
        pixel_size = pixel_size/h # pixel size in mm, calculated by width of screen (~440mm)
        print(pixel_size)
        p = desired_period / pixel_size
        
        if vert:

            x = range(w)
            z = []

            for i in x:
                value = (math.sin( x[i]*2.*math.pi/p + phase)+1)*127.
                z.append(value)

            img = np.zeros((w,h))

            for i in range(h):
                img[:,i] = z
            
        else:

            y = range(h)
            z = []

            for i in y:
                value = (math.sin( y[i]*2.*math.pi/p + phase)+1)*127.
                z.append(value)

            img = np.zeros((w,h))

            for i in range(w):
                img[i,:] = z
           

    rgb_img[...,0] = img
    rgb_img[...,1] = img
    rgb_img[...,2] = img

    cv2.imshow("Image", rgb_img)

while True:

    fringeGen(w,h);
    
    print('hey')
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()

