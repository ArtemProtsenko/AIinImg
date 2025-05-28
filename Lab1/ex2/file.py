import cv2

img = cv2.imread("image.jpg", 0)
cv2.imwrite("image2.jpg", img)
img = cv2.imread("image2.jpg")
cv2.imshow("My image", img)
cv2.waitKey()
cv2.destroyAllWindows()
