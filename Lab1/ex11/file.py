import numpy as np
import cv2

img = np.zeros((200, 550, 3), np.uint8)
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(img, "OpenCV", (0, 100), font, 4, (255, 255, 255), 4, cv2.LINE_AA)

cv2.imshow("My image", img)
cv2.waitKey()
cv2.destroyAllWindows()