import os
import cv2
import imageBackGroundRemove
import changeBackground
import addBackgorund

def show_image(img,title):
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title, 450,450)
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

imgPath='yavru-kopek.jpg'
image = cv2.imread(imgPath)
show_image(image,"orjinal")


