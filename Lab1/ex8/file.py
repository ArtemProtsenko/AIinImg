import cv2
import imutils

img = cv2.imread("image.jpg")
resized = imutils.resize(img, width=300)
cv2.rectangle(resized, (130, 85), (180, 120), (0, 0, 255), 2)

cv2.imshow("My image", resized)
cv2.waitKey()
cv2.destroyAllWindows()