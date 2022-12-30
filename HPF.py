
import cv2
from matplotlib import pyplot as plt

#img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\ImgP.bmp", 0)
#img = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\White Screen.bmp", 0)
img1 = cv2.imread("C:\\Users\\syami\\Pictures\\Basler\SolidLine Comp.bmp", 0)

scale_percent = 50 # percent of original size
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
h,w = img.shape
 
# subtract the original image with the blurred image
# after subtracting add 127 to the total result
hpf = img - cv2.GaussianBlur(img, (21, 21), 3)+127
 
# display both original image and filtered image
# cv2.imshow("Original", img)
# cv2.imshow("High Passed Filter", hpf)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(hpf, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.show()
 
# cv2.waitkey is used to display
# the image continuously
# if you provide 1000 instead of 0 then
# image will close in 1sec
# you pass in milli second
cv2.waitKey(0)
cv2.destroyAllWindows()