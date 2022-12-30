import numpy as np
import cv2
import time
import matplotlib.pyplot as plot
import screeninfo

screen_id = 1
is_color = 1

# get the size of the screen
screen = screeninfo.get_monitors()[screen_id]
width, height = screen.width, screen.height

def nothing(x):
    pass


cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',0,0)
cv2.resizeWindow("Trackbars",400,300)

cv2.createTrackbar('Period','Trackbars',10,350,nothing) 
cv2.createTrackbar('X axis','Trackbars',350,350,nothing) 
cv2.createTrackbar('Y axis','Trackbars',350,350,nothing) 
cv2.createTrackbar('Orientation','Trackbars',0,1,nothing) 

class fringe:
    def __init__(self,size_x,size_y,orientation,period):
        self.size_x = size_x
        self.size_y = size_y
        self.orientation = orientation
        self.period = period

        x = np.arange(self.size_x)  # generate 1-D sine wave of required period 
        amplitude = 1
        try:
            omega = 2*np.pi/self.period
        except:
            omega = 0
        y = amplitude *np.sin(omega * x)
        y += max(y) # offset sine wave by the max value to go out of negative range of sine 

        self.frame = np.array([[y[j]*127 for j in range(self.size_x)] for i in range(self.size_y)], dtype=np.uint8) # create 2-D array of sine-wave

        if self.orientation == 1:
            self.frame = self.frame.T

    def show(self):
        window_name = 'projector'
        cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
        cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(window_name,self.frame)


def pattern():
    if time.time() - time1 <= 2 :
        vert.show()
    elif time.time() - time1 <= 4 :
        hor.show()
    else:
        time1 = time.time()


while True:

    period=cv2.getTrackbarPos('Period','Trackbars')
    sizeX=cv2.getTrackbarPos('X axis','Trackbars')
    sizeY=cv2.getTrackbarPos('Y axis','Trackbars')
    orientation=cv2.getTrackbarPos('Orientation','Trackbars')

    vert = fringe(sizeX, sizeY, orientation, period)
    vert.show()

    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()