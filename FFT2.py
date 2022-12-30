#LOW PASS FILTER


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


# Reading image
font = cv.FONT_HERSHEY_COMPLEX
#img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\ImgP.bmp", cv2.IMREAD_COLOR)
img1= cv.imread("C:\\Users\\syami\\Pictures\\Basler\White Screen.bmp", 0)
scale_percent = 100 # percent of original size
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv.resize(img1, dim, interpolation = cv.INTER_AREA)
h,w = img.shape


dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

rows, cols = img.shape
print ("Row",rows)
print ("Col",cols)
crow,ccol = int(rows/2) , int(cols/2)
print ("Row",crow)
print ("Col",ccol)
# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows,cols,2),np.uint8)
print(mask)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv.idft(f_ishift)
img_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()