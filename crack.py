import cv2
import numpy as np
from matplotlib import pyplot as plt

# Reading image
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\ImgP.bmp", cv2.IMREAD_COLOR)
#img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\White Screen.bmp", cv2.IMREAD_COLOR)
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img1 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
h,w,c = img1.shape

blur = cv2.medianBlur(img1, 7)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,3)

canny = cv2.Canny(thresh, 120, 255, 1)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
opening = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
dilate = cv2.dilate(opening, kernel, iterations=2)

cnts = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

min_area = 500
for c in cnts:
    area = cv2.contourArea(c)
    if area > min_area:
        cv2.drawContours(img1, [c], -1, (36, 255, 12), 2)

plt.subplot(231),plt.imshow(img1, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(blur, cmap = 'gray')
plt.title('blur'), plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(gray, cmap = 'gray')
plt.title('Gray'), plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(thresh, cmap = 'gray')
plt.title('Threshold'), plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(canny, cmap = 'gray')
plt.title('canny'), plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(dilate, cmap = 'gray')
plt.title('dilate'), plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)