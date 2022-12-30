import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\ImgP.bmp", 0)
#img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\White Screen.bmp", 0)
#img1 = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\SolidLine Comp.bmp")
img1 = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\\Scratch_Line.bmp")

scale_percent = 100 # percent of original size
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
h,w,c = img.shape
 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray,50,150,apertureSize = 3)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


# hpf = gray - cv2.GaussianBlur(gray, (21, 21), 3)+127
# edges = cv2.Canny(hpf,50,150,apertureSize = 3)
# lines = cv2.HoughLines(edges,1,np.pi/180,500)
# print(lines.size)
# for line in lines:
#     rho,theta = line[0]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))
#     cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)


plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Hough Line Transform')


plt.subplot(2, 2, 2)
plt.imshow(gray, cmap='gray')
plt.title('Gray')

plt.subplot(2, 2, 3)
plt.imshow(edges, cmap='gray')
plt.title('EDGE')


# plt.subplot(2, 2, 4)
# plt.imshow(edges, cmap='gray')
# plt.title('edges')
plt.show()

cv2.waitKey(0)