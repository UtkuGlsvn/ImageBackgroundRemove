import cv2

image = cv2.imread('output.png', cv2.IMREAD_UNCHANGED)    


trans_mask = image[:,:,3] == 0


image[trans_mask] = [255, 0, 0, 0]


new_img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
cv2.imwrite("outImgPy3.png", new_img)

cv2.waitKey(0)
