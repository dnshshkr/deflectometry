from pypylon import pylon
import cv2
import matplotlib.pyplot as plt


#camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera=cv2.VideoCapture(0)
camera.open()
img = camera.GrabOne(4000)
img = img.Array
print(img.shape)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
plt.show()
#cv2.waitKey(0)