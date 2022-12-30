# gratings.py

import numpy as np
import matplotlib.pyplot as plt
import cv2

x = np.arange(-500, 501, 1)

X, Y = np.meshgrid(x, x)

wavelength = 200
grating = np.sin(2 * np.pi * X / wavelength)

# plt.set_cmap("gray")
# plt.imshow(grating)
# plt.show()

cv2.imshow("Frame",grating)
cv2.waitKey(0)