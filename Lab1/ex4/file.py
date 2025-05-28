import cv2

img = cv2.imread("image.jpg")
roi = img[200:270, 320:420]
cv2.imshow("My image", roi)
cv2.waitKey()
cv2.destroyAllWindows()