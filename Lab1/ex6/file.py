import cv2
import imutils

img = cv2.imread("image.jpg")
resized = imutils.resize(img, width=300)
h, w = resized.shape[0:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 24, 1.0)
rotated = cv2.warpAffine(resized, M, (w, h))
cv2.imshow("My image", rotated)
cv2.waitKey()
cv2.destroyAllWindows()
