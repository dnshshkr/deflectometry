"""
Capture projection pattern and decode x-coorde.
"""
import cv2
import numpy as np
import structuredlight as sl
import screeninfo
from pypylon import pylon
from matplotlib import pyplot as plt

screen_id = 2
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
    scale_percent = 100 # percent of original size
    width2 = int(5472 * scale_percent / 100)
    height2 = int(3648 * scale_percent / 100)
    dim = (width2, height2)
    
    # resize image
    img_gray = cv2.resize(img_gray, dim, interpolation = cv2.INTER_AREA)
    #img_gray = img_gray[y1:y2, x1:x2]
    # ret, img_gray = cv2.threshold(img_gray, 30, 255, cv2.THRESH_TOZERO)
    cv2.namedWindow("img_gray", cv2.WND_PROP_FULLSCREEN);cv2.setWindowProperty("img_gray", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);cv2.imshow("img_gray", img_gray);cv2.moveWindow("img_gray",0,0)
    # cv2.waitKey(0)
    # print(img_gray.shape)
    # img_gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)
    return img_gray

def main():
    try:
        cap = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        cap.Open()
    except:
        cap = cv2.VideoCapture(1) # External web camera
        cap.open
    num=5
    F:int=20
    num1=num
    F1=F
    phaseshifting = sl.PhaseShifting(num1,F1)
   
    imlist_posi_x_pat = phaseshifting.generate((width, height))
    print(imlist_posi_x_pat)

    # Capture
    imlist_posi_x_cap = [imshowAndCapture(cap, img) for img in imlist_posi_x_pat]
    
    # addPicture = 0
    # for i in range (num):
    #     print(i)
    #     addPicture = cv2.add(addPicture, imlist_posi_x_cap[i])
    #     i=i+1
    
    # plt.imshow(addPicture, cmap='gray')
    # plt.title('addPicture')
    # plt.show()

    # Decode
    img_index_x = phaseshifting.decodeAmplitude(imlist_posi_x_cap)

    
    num2=num
    #F2=int(20*9/16)
    F2=int(float(F)*9/16)
    phaseshifting = sl.PhaseShifting(num2,F2)

    # Generate and Decode y-coord
    imlist = phaseshifting.generate((width, height))
    
    imlist_posi_y_pat = sl.transpose(imlist)
    # imlist_posi_y_pat = sl.invert(imlist_posi_y_pat)

    # Capture
    imlist_posi_y_cap = [ imshowAndCapture(cap, img) for img in imlist_posi_y_pat]
    
    # Decode
    img_index_y = phaseshifting.decodeAmplitude(imlist_posi_y_cap)
   

    # Visualize decode result
    img_correspondence = cv2.merge([0.0*np.zeros_like(img_index_x), img_index_x/width, img_index_y/height])
    #img_correspondence = cv2.merge([0.0*np.zeros_like(img_index_x), img_index_x, img_index_y])
    img_correspondence = np.clip(img_correspondence*255.0, 0, 255).astype(np.uint8)

    img_correspondence = cv2.cvtColor(img_correspondence, cv2.COLOR_BGR2GRAY)
    plt.imsave('imgXY.png',img_correspondence,cmap='gray')


    x1=2000
    x2=4500
    y1=400
    y2=2000

    # x1=1500
    # x2=3250
    # y1=300
    # y2=1500

    plt.subplot(1, 3, 1)
    plt.imshow(img_correspondence, cmap='gray')
    plt.title('Combine Index XY')
    # plt.xlim([x1,x2])
    # plt.ylim([y1,y2])

    # plt.subplot(1, 2, 1)
    # plt.imshow(img_index_x, cmap='gray')
    # plt.title('img_index_x Num: '+ str(num1) + " and F: " + str(F1))

    plt.subplot(1, 3, 2)
    plt.imshow(img_index_x, cmap='gray')
    # plt.xlim([x1,x2])
    # plt.ylim([y1,y2])
    plt.title('img_index_x Num: '+ str(num1) + " and F: " + str(F1))

    plt.subplot(1, 3, 3)
    plt.imshow(img_index_y, cmap='gray')
    plt.title('img_index_y Num: '+ str(num2) + " and F: " + str(F2))
    # plt.xlim([x1,x2])
    # plt.ylim([y1,y2])

    plt.show()
    cv2.destroyAllWindows()
    plt.imsave('imgXY.png',img_correspondence,cmap='gray')
    # cap.release()

if __name__=="__main__":
    main()