import cv2
import imutils
import numpy as np

img = cv2.imread("image.jpg")
resized = imutils.resize(img, width=300)
blurred = cv2.GaussianBlur(resized, (11, 11), 0)
summing = np.hstack((resized, blurred))
cv2.imshow("My image", summing)
cv2.waitKey()
cv2.destroyAllWindows()