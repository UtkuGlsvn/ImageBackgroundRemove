import cv2

def show_image(img,title):
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title, 450,450)
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


dsize = (500, 500)

foreGroundImage = cv2.imread("output/bgclear.png", -1)
foreGroundImage = cv2.resize(foreGroundImage, dsize)


b,g,r,a = cv2.split(foreGroundImage)

foreground = cv2.merge((b,g,r))

alpha = cv2.merge((a,a,a))


background = cv2.imread("denizKenari.jpg")

background = cv2.resize(background, dsize)

foreground = foreground.astype(float)
background = background.astype(float)
alpha = alpha.astype(float)/255

foreground = cv2.multiply(alpha, foreground)
background = cv2.multiply(1.0 - alpha, background)
outImage = cv2.add(foreground, background)

cv2.imwrite("output/addBgimg.png", outImage)
show_image(outImage/255,"addbg")
cv2.waitKey(0)