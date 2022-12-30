"""
Capture projection pattern and decode x-coorde.
"""
import cv2
import numpy as np
import structuredlight as sl
import screeninfo
from pypylon import pylon
from matplotlib import pyplot as plt

screen_id = 1
is_color = 1

# get the size of the screen
screen = screeninfo.get_monitors()[screen_id]
width, height = screen.width, screen.height

x1=2900
x2=3400
y1=600
y2=1400

def imshowAndCapture(cap, img_pattern, delay=250):
    window_name = 'projector'
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(window_name, img_pattern)
    cv2.waitKey(delay)
    # ret, img_frame = cap.read()

    img_frame = cap.GrabOne(4000)
    img_gray = img_frame.Array 
    scale_percent = 80 # percent of original size
    width2 = int(5472 * scale_percent / 100)
    height2 = int(3648 * scale_percent / 100)
    dim = (width2, height2)
    # resize image
    img_gray = cv2.resize(img_gray, dim, interpolation = cv2.INTER_AREA)


    #img_gray = img_gray[y1:y2, x1:x2]
    # ret, img_gray = cv2.threshold(img_gray, 50, 255, cv2.THRESH_TOZERO)
    cv2.namedWindow("img_gray", cv2.WND_PROP_FULLSCREEN);cv2.setWindowProperty("img_gray", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);cv2.imshow("img_gray", img_gray);cv2.moveWindow("img_gray",0,0)
    cv2.waitKey(0)
    # print(img_gray.shape)
    # img_gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)
    return img_gray

def main():

    # cap = cv2.VideoCapture(0) # External web camera
    cap = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
    cap.Open()
    num=2
    F=30.0
    phaseshifting = sl.PhaseShifting(num,F)
   
    imlist_posi_x_pat = phaseshifting.generate((width, height))

    # Capture
    imlist_posi_x_cap = [ imshowAndCapture(cap, img) for img in imlist_posi_x_pat]
    
    addPicture = 0
    for i in range (num):
        print(i)
        addPicture = cv2.add(addPicture, imlist_posi_x_cap[i])
        i=i+1
    
    plt.imshow(addPicture, cmap='gray')
    plt.title('addPicture')
    plt.show()

    h = int(3648 *0.8)
    w = int(5472 *0.8)
    img_white = np.full((h, w), 255, dtype=np.uint8)
    img_black = np.full((h, w),  0 , dtype=np.uint8)
    img_thresh = 0.5*img_white + 0.5*img_black
    img_index = phaseshifting.binarize(addPicture, thresh=imlist_posi_x_cap[0])


    plt.imshow(img_index, cmap='gray')
    plt.title('img_index')
    plt.show()

    img_correspondence = phaseshifting.decodeAmplitude(imlist_posi_x_cap)
   

    # Visualize decode result
    # img_correspondence = cv2.merge([0.0*np.zeros_like(img_index_x), img_index_x/width, img_index_y/height])
    img_correspondence = np.clip(img_correspondence*255.0, 0, 255).astype(np.uint8)


    plt.imshow(img_correspondence, cmap='gray')
    plt.show()
    cv2.destroyAllWindows()
    # cap.release()

if __name__=="__main__":
    main()