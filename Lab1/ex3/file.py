import cv2

img = cv2.imread("image.jpg")
(blue, red, green) = img[100, 50]
print(f"{ red = }, { green = }, { blue = }")
