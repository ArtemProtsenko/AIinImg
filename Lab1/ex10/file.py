import numpy as np
import cv2

img = np.zeros((200, 200, 3), np.uint8)
cv2.circle(img, (100, 100), 50, (0, 0, 255), 2)
cv2.imshow("My image", img)
cv2.waitKey()
cv2.destroyAllWindows()