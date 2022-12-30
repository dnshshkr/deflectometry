import cv2
import numpy as np
import screeninfo

screen_id = 1
is_color = 1

# get the size of the screen
screen = screeninfo.get_monitors()[screen_id]
width, height = screen.width, screen.height

img_1 = np.zeros([width,height,1],dtype=np.uint8)
img_1.fill(255) #255 or 0
cv2.namedWindow("Fringe", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Fringe",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

cv2.moveWindow("Fringe",1920,0)
cv2.imshow('Fringe', img_1)
print("image shape: ", img_1.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()