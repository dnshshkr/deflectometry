import numpy as np
import matplotlib.pyplot as plt
import cv2

N = 256
x = np.linspace(-np.pi,np.pi, N)
sine1D = 128.0 + (127.0 * np.sin(x * 8.0))
print(sine1D)
sine1D = np.uint8(sine1D)
print(sine1D)
sine2D = np.tile(sine1D, (N,1))
print(sine2D.shape)
# plt.imshow(sine2D, cmap='gray')
# plt.show()
cv2.namedWindow("Fringe", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Fringe",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.moveWindow("Fringe",1920,0)
cv2.imshow('Fringe',sine2D)

while True:
    
    if cv2.waitKey()==ord('q'):
        break

cv2.destroyAllWindows()
