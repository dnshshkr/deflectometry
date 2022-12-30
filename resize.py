import cv2
import numpy as np
from matplotlib import pyplot as plt

for i in range(28):
    
    print (i)
    if i < 10:
        filename = "pat0" + str(i) + ".png"
    else:
        filename = "pat" + str(i) + ".png"

    print (filename)

    img1 = cv2.imread("C:\\Users\\syami\\deflectrometry\\phase-shifting\\Data\\" + filename)

    scale_percent = 50 # percent of original size
    width = int(img1.shape[1] * scale_percent / 100)
    height = int(img1.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
    h,w,c = img.shape
    print("shape: ",img.shape)
    print("size: ",img.size)
    cv2.imwrite("C:\\Users\\syami\\deflectrometry\\phase-shifting\\Data\\Resize 50\\" + filename,img)