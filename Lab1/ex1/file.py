import cv2

img = cv2.imread("image.jpg")

cv2.imshow("My image", img)
cv2.waitKey()
cv2.destroyAllWindows()
