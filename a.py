import cv2

dsize = (500, 500)

foreGroundImage = cv2.imread("output.png", -1)
foreGroundImage = cv2.resize(foreGroundImage, dsize)


b,g,r,a = cv2.split(foreGroundImage)

foreground = cv2.merge((b,g,r))

alpha = cv2.merge((a,a,a))


background = cv2.imread("denizkenari.jpg")

background = cv2.resize(background, dsize)

foreground = foreground.astype(float)
background = background.astype(float)
alpha = alpha.astype(float)/255

foreground = cv2.multiply(alpha, foreground)
background = cv2.multiply(1.0 - alpha, background)
outImage = cv2.add(foreground, background)

cv2.imwrite("outImgPy.png", outImage)

cv2.imshow("outImg", outImage/255)
cv2.waitKey(0)
