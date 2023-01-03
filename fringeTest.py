import numpy as np
import cv2
import time
import matplotlib.pyplot as plot


class fringe:
    def __init__(self,size_x,size_y,orientation,period):
        self.size_x = size_x
        self.size_y = size_y
        self.orientation = orientation
        self.period = period

        x = np.arange(self.size_x)  # generate 1-D sine wave of required period 
        amplitude = 1
        period = 20
        omega = 2*np.pi/self.period
        y = amplitude *np.sin(omega * x)
        y += max(y) # offset sine wave by the max value to go out of negative range of sine
        self.frame = np.array([[y[j]*127 for j in range(self.size_x)] for i in range(self.size_y)], dtype=np.uint8) # create 2-D array of sine-wave
        if self.orientation == 'Vertical':
            self.frame = self.frame.T

    def show(self):
        cv2.namedWindow("Fringe", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Fringe",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

        cv2.imshow("Fringe",self.frame)
        cv2.moveWindow("Fringe",1920,0)
        if self.orientation == "Vertical":
            self.shifted_frame =  np.roll(self.frame, 2, axis=0) # roll the columns of the sine wave to get moving effect
        else:
            self.shifted_frame =  np.roll(self.frame, 2, axis=1) # roll the columns of the sine wave to get moving effect
        self.frame = self.shifted_frame 


sizeX = 350
sizeY= 350

vert = fringe(sizeX, sizeY, 'Vertical', 50)
hor = fringe(sizeY, sizeX, 'Hor', 50)

time1 = time.time()

while True:
    time.sleep(0.1)
    if time.time() - time1 <= 2 :
        vert.show()
    elif time.time() - time1 <= 4 :
        hor.show()
    else:
        time1 = time.time()

    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()