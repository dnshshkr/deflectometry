import numpy as np
from structuredlight import StructuredLight
from matplotlib import pyplot as plt
import cv2
import screeninfo
from pypylon import pylon

screen_id = 1
is_color = 1

# get the size of the screen
screen = screeninfo.get_monitors()[screen_id]
width, height = screen.width, screen.height

class Stripe(StructuredLight):
    def generate(self, dsize):
        width, height = dsize
        num = width

        imgs_code = 255*np.fromfunction(lambda y,x,n: x==n, (height, width, num), dtype=int).astype(np.uint8)
        imlist = self.split(imgs_code)
        

        return imlist

    def decode(self, imlist):
        img_index = np.argmax(imlist, axis=0)
        return img_index

cap = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
cap.Open()

sl=Stripe()
imlist = sl.generate((50,5))

index = 20

window_name = 'projector'
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow(window_name, (imlist[index]))
cv2.waitKey(250)
img_frame = cap.GrabOne(4000)
img_gray = img_frame.Array 
scale_percent = 100 # percent of original size
width2 = int(5472 * scale_percent / 100)
height2 = int(3648 * scale_percent / 100)
dim = (width2, height2)
img_gray = cv2.resize(img_gray, dim, interpolation = cv2.INTER_AREA)
ret, img_gray1 = cv2.threshold(img_gray, 50, 255, cv2.THRESH_TOZERO)
cv2.namedWindow("img_gray", cv2.WND_PROP_FULLSCREEN);cv2.setWindowProperty("img_gray", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);cv2.imshow("img_gray", img_gray1);cv2.moveWindow("img_gray",0,0)
cv2.waitKey(0)


imlist = sl.generate((50,5))

window_name = 'projector'
black = 0 * np.ones((2,1), np.uint8)
imlist[index] = np.insert(imlist[index], 0, black, axis=1)

cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow(window_name, (imlist[index]))
cv2.waitKey(250)
img_frame = cap.GrabOne(4000)
img_gray = img_frame.Array 
scale_percent = 100 # percent of original size
width2 = int(5472 * scale_percent / 100)
height2 = int(3648 * scale_percent / 100)
dim = (width2, height2)
img_gray = cv2.resize(img_gray, dim, interpolation = cv2.INTER_AREA)
ret, img_gray2 = cv2.threshold(img_gray, 50, 255, cv2.THRESH_TOZERO)
cv2.namedWindow("img_gray", cv2.WND_PROP_FULLSCREEN);cv2.setWindowProperty("img_gray", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);cv2.imshow("img_gray", img_gray2);cv2.moveWindow("img_gray",0,0)
cv2.waitKey(0)

imlist = sl.generate((50,5))

window_name = 'projector'
black = 0 * np.ones((4,1), np.uint8)
imlist[index] = np.insert(imlist[index], 0, black, axis=1)

cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow(window_name, (imlist[index]))
cv2.waitKey(250)
img_frame = cap.GrabOne(4000)
img_gray = img_frame.Array 
scale_percent = 100 # percent of original size
width2 = int(5472 * scale_percent / 100)
height2 = int(3648 * scale_percent / 100)
dim = (width2, height2)
img_gray = cv2.resize(img_gray, dim, interpolation = cv2.INTER_AREA)
ret, img_gray3 = cv2.threshold(img_gray, 50, 255, cv2.THRESH_TOZERO)
cv2.namedWindow("img_gray", cv2.WND_PROP_FULLSCREEN);cv2.setWindowProperty("img_gray", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);cv2.imshow("img_gray", img_gray3);cv2.moveWindow("img_gray",0,0)
cv2.waitKey(0)

addPicture = cv2.add(img_gray1, img_gray2)
addPicture = cv2.add(addPicture,img_gray3)
plt.imshow(addPicture, cmap='gray')
plt.title('addPicture')
plt.show()
