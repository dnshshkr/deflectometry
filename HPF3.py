
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
 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# dimension of gray image is in 2D
dimensions = gray.shape  # (height,weight)
 
print("Image Dimensions:", dimensions)
n = int(input("Enter the size of the original image to be captured:"))
print("The matrix of the original image:")
 
 
for i in range(0, n):
    for j in range(0, n):
        print(gray[i][j], end=" ")
    print()
"""
Apply below filter on image matrix
0 -1 0
-1 4 -1
0  -1 0
"""
filter = np.zeros(shape=(n, n))
for i in range(0, n):
    for j in range(0, n):
        filter[i][j] = 0*gray[i][j]-1*gray[i][j+1]\
        +0*gray[i][j+2]-1*gray[i+1][j]+4 * \
            gray[i+1][j+1]-1*gray[i+1][j+2]+0*gray[i+2][j] - \
            1*gray[i+2][j+1]+0*gray[i+2][j+2]
 
print("\n")
print("The matrix form after HPF masking the captured image is:")
print("\n")
for hpf in filter:
    print(hpf)

img2 = cv2.filter2D(src=gray, ddepth=-1, kernel=filter)

# plot images
plt.subplot(1, 2, 1)
plt.imshow(img1, cmap='gray')
plt.title('Ori')
 
plt.subplot(1, 2, 2)
plt.imshow(img2, cmap='gray')
plt.title('gray')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()