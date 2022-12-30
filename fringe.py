import cv2
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc


x = np.arange(1)  # generate 1-D sine wave of required period 
amplitude = 1
period = 20
omega = 2*np.pi/period

y = amplitude *np.sin(omega * x)

y += max(y) # offset sine wave by the max value to go out of negative range of sine 

frame = np.array([[y[j]*127 for j in range(346)] for i in range(260)], dtype=np.uint8) # create 2-D array of sine-wave

while True:

    cv2.imshow("Fringe",frame)
    shifted_frame =  np.roll(frame, 2, axis=1) # roll the columns of the sine wave to get moving effect
    frame = shifted_frame 
    
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()
