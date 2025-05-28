import cv2
import numpy

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.startWindowThread()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture("vid.mp4")

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (800, 500))
    gray_filter = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    boxes, weights = hog.detectMultiScale(gray_filter, winStride=(8, 8))
    boxes = numpy.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    for (xa, ya, xb, yb) in boxes:
        cv2.rectangle(frame, (xa, ya), (xb, yb), (0, 255, 255), 2)

    face_rects = face_cascade.detectMultiScale(gray_filter, 1.1, 5)
    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)

    cv2.imshow('Video', frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
