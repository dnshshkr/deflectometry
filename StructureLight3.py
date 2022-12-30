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
    scale_percent = 60 # percent of original size
    width = int(5472 * scale_percent / 100)
    height = int(3648 * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    img_gray = cv2.resize(img_gray, dim, interpolation = cv2.INTER_AREA)

    ret, img_gray = cv2.threshold(img_gray, 50, 255, cv2.THRESH_TOZERO)
    cv2.namedWindow("img_gray", cv2.WND_PROP_FULLSCREEN);cv2.setWindowProperty("img_gray", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);cv2.imshow("img_gray", img_gray);cv2.moveWindow("img_gray",0,0)
    #cv2.waitKey(0)
    # print(img_gray.shape)
    # img_gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)
    return img_gray

def main():
    width  = 50
    height = 50

    # cap = cv2.VideoCapture(0) # External web camera
    cap = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
    cap.Open()
    gray = sl.Gray()
   
        # Generate and Decode x-coord
    # Generate
    imlist_posi_x_pat = gray.generate((width, height))
    imlist_nega_x_pat = sl.invert(imlist_posi_x_pat)

    # Capture
    imlist_posi_x_cap = [ imshowAndCapture(cap, img) for img in imlist_posi_x_pat]
    imlist_nega_x_cap = [ imshowAndCapture(cap, img) for img in imlist_nega_x_pat]
    
    addPicture = 0
    for i in range (len(imlist_posi_x_cap)):
        print(i)
        addPicture = cv2.add(addPicture, imlist_posi_x_cap[i])
        i=i+1
    
    plt.imshow(addPicture, cmap='gray')
    plt.title('addPicture')
    plt.show()

    # Decode
    img_index_x = gray.decode(imlist_posi_x_cap, imlist_nega_x_cap)
    
    
    # Generate and Decode y-coord
    # Generate
    imlist = gray.generate((height, width))
    imlist_posi_y_pat = sl.transpose(imlist)
    imlist_nega_y_pat = sl.invert(imlist_posi_y_pat)
    
    # Capture
    imlist_posi_y_cap = [ imshowAndCapture(cap, img) for img in imlist_posi_y_pat]
    imlist_nega_y_cap = [ imshowAndCapture(cap, img) for img in imlist_nega_y_pat]
    
    # Decode
    img_index_y = gray.decode(imlist_posi_y_cap, imlist_nega_y_cap)
   

    # Visualize decode result
    img_correspondence = cv2.merge([0.0*np.zeros_like(img_index_x), img_index_x/width, img_index_y/height])
    img_correspondence = np.clip(img_correspondence*255.0, 0, 255).astype(np.uint8)
    img_correspondence = cv2.cvtColor(img_correspondence, cv2.COLOR_BGR2GRAY)

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