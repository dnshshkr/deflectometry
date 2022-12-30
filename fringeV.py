import cv2
import numpy as np

size_x = 360
size_y = 260
x = np.arange(size_x)  # generate 1-D sine wave of required period 
amplitude = 1
period = 20
omega = 2*np.pi/period
y = amplitude *np.sin(omega * x)
y += max(y) # offset sine wave by the max value to go out of negative range of sine 

frame = np.array([[y[j]*127 for j in range(size_x)] for i in range(size_y)], dtype=np.uint8) # create 2-D array of sine-wave

frame = frame.T

while True:

    cv2.imshow("Fringe",frame)
    shifted_frame =  np.roll(frame, 2, axis=0) # roll the columns of the sine wave to get moving effect
    frame = shifted_frame 
    
    
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()
