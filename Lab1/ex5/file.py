import cv2

img = cv2.imread("image.jpg")
h, w = img.shape[0:2]
h_new = 300
ratio = w / h
w_new = int(h_new * ratio)
resized = cv2.resize(img, (w_new, h_new))
cv2.imshow("My image", resized)
cv2.waitKey()
cv2.destroyAllWindows()
