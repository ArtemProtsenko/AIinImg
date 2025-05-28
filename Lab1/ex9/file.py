import numpy as np
import cv2

img = np.zeros((200, 200, 3), np.uint8)

cv2.line(img, (0, 0), (200, 200), (255, 0, 0), 5)

points = np.array([[0, 0], [100, 50], [50, 100], [0, 0]])
cv2.polylines(img, np.int32([points]), 1, (255, 255, 255))

cv2.imshow("My image", img)
cv2.waitKey()
cv2.destroyAllWindows()