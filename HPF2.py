import cv2
from matplotlib import pyplot as plt

#img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\ImgP.bmp", 0)
#img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\White Screen.bmp", 0)
img1 = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\SolidLine Comp.bmp")

scale_percent = 50 # percent of original size
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
h,w,c = img.shape

# convert image to gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# apply laplacian blur
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
 
# sobel x filter where dx=1 and dy=0
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=7)
 
# sobel y filter where dx=0 and dy=1
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=7)
 
# combine sobel x and y
sobel = cv2.bitwise_and(sobelx, sobely)
 
# plot images
plt.subplot(2, 2, 1)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian')
 
plt.subplot(2, 2, 2)
plt.imshow(sobelx, cmap='gray')
plt.title('SobelX')
 
plt.subplot(2, 2, 3)
plt.imshow(sobely, cmap='gray')
plt.title('SobelY')
 
plt.subplot(2, 2, 4)
plt.imshow(sobel, cmap='gray')
plt.title('Sobel')
 
plt.show()
 
cv2.waitKey(0)
cv2.destroyAllWindows()