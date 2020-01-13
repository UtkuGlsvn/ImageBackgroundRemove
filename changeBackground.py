import cv2

def show_image(img,title):
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title, 450,450)
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image = cv2.imread('output/bgclear.png', cv2.IMREAD_UNCHANGED)    

trans_mask = image[:,:,3] == 0


image[trans_mask] = [255, 0, 0, 0]


new_img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
cv2.imwrite("output/changebgcolor.png",new_img )
show_image(new_img,"addcolorbg")
cv2.waitKey(0)
