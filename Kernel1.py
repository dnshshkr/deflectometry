# importing the modules needed
import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\ImgP.bmp", 0)
#img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\White Screen.bmp", 0)
img1 = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\SolidLine Comp.bmp")

scale_percent = 100 # percent of original size
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
h,w,c = img.shape
 
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# Creating the kernel(2d convolution matrix)
edge = np.array([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1, -1]])

mean_filter = np.ones((3,3))
# creating a gaussian filter
x = cv2.getGaussianKernel(5,10)
gaussian = x*x.T
# different edge detecting filters
# scharr in x-direction
scharr = np.array([[-3, 0, 3],
                   [-10,0,10],
                   [-3, 0, 3]])
# sobel in x direction
sobel_x= np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
# sobel in y direction
sobel_y= np.array([[-1,-2,-1],
                   [0, 0, 0],
                   [1, 2, 1]])
# laplacian
laplacian=np.array([[0, 1, 0],
                    [1,-4, 1],
                    [0, 1, 0]])

# Applying the filter2D() function
img1 = cv2.filter2D(src=image, ddepth=-1, kernel=edge)
img2 = cv2.filter2D(src=image, ddepth=-1, kernel=mean_filter)
img3 = cv2.filter2D(src=image, ddepth=-1, kernel=gaussian)
img4 = cv2.filter2D(src=image, ddepth=-1, kernel=scharr)
img5 = cv2.filter2D(src=image, ddepth=-1, kernel=sobel_x)
img6 = cv2.filter2D(src=image, ddepth=-1, kernel=sobel_y)
img7 = cv2.filter2D(src=image, ddepth=-1, kernel=laplacian)
  
# Shoeing the original and output image
# plot images
plt.subplot(2, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Ori')
 
plt.subplot(2, 4, 2)
plt.imshow(img1, cmap='gray')
plt.title('edge')

plt.subplot(2, 4, 3)
plt.imshow(img2, cmap='gray')
plt.title('mean_filter')

plt.subplot(2, 4, 4)
plt.imshow(img3, cmap='gray')
plt.title('gaussian')

plt.subplot(2, 4, 5)
plt.imshow(img4, cmap='gray')
plt.title('scharr')

plt.subplot(2, 4, 6)
plt.imshow(img5, cmap='gray')
plt.title('sobel_x')

plt.subplot(2, 4, 7)
plt.imshow(img6, cmap='gray')
plt.title('sobel_y')

plt.subplot(2, 4, 8)
plt.imshow(img7, cmap='gray')
plt.title('laplacian')

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()