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
    img_gray = img_gray[y1:y2, x1:x2]
    cv2.namedWindow("img_gray", cv2.WND_PROP_FULLSCREEN);cv2.setWindowProperty("img_gray", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);cv2.imshow("img_gray", img_gray);cv2.moveWindow("img_gray",0,0)
    #cv2.waitKey(0)
    # print(img_gray.shape)
    # img_gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)
    return img_gray

def main():

    # cap = cv2.VideoCapture(0) # External web camera
    cap = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
    cap.Open()
    num=5
    F=100.0
    phaseshifting = sl.PhaseShifting(num,F)
   
    imlist_posi_x_pat = phaseshifting.generate((width, height))

    # Capture
    imlist_posi_x_cap = [ imshowAndCapture(cap, img) for img in imlist_posi_x_pat]
    
    # Decode
    img_index_x = phaseshifting.decode(imlist_posi_x_cap)

    
    num=5
    F=50.0
    phaseshifting = sl.PhaseShifting(num,F)

    # Generate and Decode y-coord
    imlist = phaseshifting.generate((width, height))
    
    imlist_posi_y_pat = sl.transpose(imlist)
    # imlist_posi_y_pat = sl.invert(imlist_posi_y_pat)

    # Capture
    imlist_posi_y_cap = [ imshowAndCapture(cap, img) for img in imlist_posi_y_pat]
    
    # Decode
    img_index_y = phaseshifting.decode(imlist_posi_y_cap)
   

    # Visualize decode result
    img_correspondence = cv2.merge([0.0*np.zeros_like(img_index_x), img_index_x/width, img_index_y/height])
    img_correspondence = np.clip(img_correspondence*255.0, 0, 255).astype(np.uint8)

    img_correspondence = cv2.cvtColor(img_correspondence, cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(img_correspondence, cv2.CV_64F)
    laplacianx = cv2.Laplacian(img_index_x, cv2.CV_64F)
    laplaciany = cv2.Laplacian(img_index_y, cv2.CV_64F)

    x1=2900
    x2=3400
    y1=600
    y2=1400

    plt.subplot(1, 3, 1)
    plt.imshow(img_correspondence, cmap='gray')
    plt.title('Num: '+ str(num) + " and F: " + str(F))
    # plt.xlim([x1,x2])
    # plt.ylim([y1,y2])

    plt.subplot(1, 3, 2)
    plt.imshow(img_index_x, cmap='gray')
    plt.xlim([x1,x2])
    plt.ylim([y1,y2])
    plt.title('img_index_x')

    plt.subplot(1, 3, 3)
    plt.imshow(img_index_y, cmap='gray')
    plt.title('img_index_y')
    plt.xlim([x1,x2])
    plt.ylim([y1,y2])

    # plt.subplot(2, 3, 4)
    # plt.imshow(laplacian, cmap='gray')
    # plt.title('laplacian')
    # plt.xlim([x1,x2])
    # plt.ylim([y1,y2])

    # plt.subplot(2, 3, 5)
    # plt.imshow(laplacianx, cmap='gray')
    # plt.title('laplacianx')
    # plt.xlim([x1,x2])
    # plt.ylim([y1,y2])

    # plt.subplot(2, 3, 6)
    # plt.imshow(laplaciany, cmap='gray')
    # plt.title('laplaciany')
    # plt.xlim([x1,x2])
    # plt.ylim([y1,y2])
    

    plt.show()
    #cv2.imshow("corresponnence map", img_correspondence)
    # cv2.waitKey(0)
    #cv2.imwrite("correspondence.png", img_correspondence)
    cv2.destroyAllWindows()
    # cap.release()

if __name__=="__main__":
    main()