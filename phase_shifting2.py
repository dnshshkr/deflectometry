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
    scale_percent = 50 # percent of original size
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
    num=5
    F=1.0
    phaseshifting = sl.PhaseShifting(num,F)
   
    # Generate and Decode x-coord
    # Generate
    # imlist_posi_x_pat = gray.generate((width, height))
    # imlist_nega_x_pat = sl.invert(imlist_posi_x_pat)

    imlist_posi_x_pat = phaseshifting.generate((width, height))
    imlist_nega_x_pat = sl.invert(imlist_posi_x_pat)

    # Capture
    imlist_posi_x_cap = [ imshowAndCapture(cap, img) for img in imlist_posi_x_pat]
    #imlist_nega_x_cap = [ imshowAndCapture(cap, img) for img in imlist_nega_x_pat]
    
    # Decode
    img_index_x = phaseshifting.decode(imlist_posi_x_cap)

    
    # Generate and Decode y-coord
    # Generate
    # imlist = gray.generate((height, width))
    imlist = phaseshifting.generate((height, width))
    
    imlist_posi_y_pat = sl.transpose(imlist)
    imlist_nega_y_pat = sl.invert(imlist_posi_y_pat)
    
    # Capture
    imlist_posi_y_cap = [ imshowAndCapture(cap, img) for img in imlist_posi_y_pat]
    
    # Decode
    img_index_y = phaseshifting.decode(imlist_posi_y_cap)
   

    # Visualize decode result
    img_correspondence = cv2.merge([0.0*np.zeros_like(img_index_x), img_index_x/width, img_index_y/height])
    img_correspondence = np.clip(img_correspondence*255.0, 0, 255).astype(np.uint8)

    img_correspondence = cv2.cvtColor(img_correspondence, cv2.COLOR_BGR2GRAY)

    f = np.fft.fft2(img_correspondence)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    plt.subplot(121),plt.imshow(img_correspondence, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    
    rows, cols = img_correspondence.shape
    crow,ccol = rows//2 , cols//2
    fshift[crow-30:crow+31, ccol-30:ccol+31] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.real(img_back)
    plt.subplot(131),plt.imshow(img_correspondence, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
    plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(img_back)
    plt.title('Result in JET'), plt.xticks([]), plt.yticks([])

    # plt.subplot(2, 3, 1)
    # plt.imshow(img_correspondence, cmap='gray')
    # plt.title('Num: '+ str(num) + " and F: " + str(F))
    # plt.subplot(2, 3, 2)
    # plt.imshow(laplacian, cmap='gray')
    # plt.title('laplacian')
  

    plt.show()
    #cv2.imshow("corresponnence map", img_correspondence)
    # cv2.waitKey(0)
    #cv2.imwrite("correspondence.png", img_correspondence)
    cv2.destroyAllWindows()
    # cap.release()

if __name__=="__main__":
    main()