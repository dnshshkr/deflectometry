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
    scale_percent = 65 # percent of original size
    width = int(5472 * scale_percent / 100)
    height = int(3648 * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    img_gray = cv2.resize(img_gray, dim, interpolation = cv2.INTER_AREA)


    # print(img_gray.shape)
    # img_gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)
    return img_gray

def main():
    width  = 1920
    height = 1080

    # cap = cv2.VideoCapture(0) # External web camera
    cap = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
    cap.Open()
    gray = sl.Gray()
   
    # Generate and Decode x-coord
    # Generate
    imlist_posi_pat = gray.generate((width, height))
    imlist_nega_pat = sl.invert(imlist_posi_pat)

    # Capture
    imlist_posi_cap = [ imshowAndCapture(cap, img) for img in imlist_posi_pat]
    imlist_nega_cap = [ imshowAndCapture(cap, img) for img in imlist_nega_pat]
    
    # Decode
    img_index = gray.decode(imlist_posi_cap, imlist_nega_cap)

    # Visualize decode result
    img_correspondence = np.clip(img_index/width*255.0, 0, 255).astype(np.uint8)
    plt.imshow(img_correspondence, cmap='gray')
    plt.title('img_correspondence')
    plt.show()
    #cv2.imshow("corresponnence map", img_correspondence)
    # cv2.waitKey(0)
    #cv2.imwrite("correspondence.png", img_correspondence)
    cv2.destroyAllWindows()
    # cap.release()

if __name__=="__main__":
    main()