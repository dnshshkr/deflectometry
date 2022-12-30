#HIGH PASS FILTER

import cv2
import numpy as np
from matplotlib import pyplot as plt


# Reading image
font = cv2.FONT_HERSHEY_COMPLEX
#img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\ImgP.bmp", 0)
#img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\White Screen.bmp", 0)
img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\SolidLine Comp.bmp", 0)

scale_percent = 50 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img1 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
h,w = img1.shape

f = np.fft.fft2(img1)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img1, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

rows, cols = img1.shape
crow,ccol = rows//2 , cols//2
fshift[crow-30:crow+31, ccol-30:ccol+31] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.real(img_back)
plt.subplot(131),plt.imshow(img1, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()
