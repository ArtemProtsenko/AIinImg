import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

scaling_factor = 0.5
frame = cv2.imread('image.jpg')

gray_filter = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

face_rects = face_cascade.detectMultiScale(gray_filter, 1.1, 5)
for (x, y, w, h) in face_rects:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray_filter[y:y + h, x:x + w]
    roi_color = frame[y:y + h, x:x + w]
    smile = smile_cascade.detectMultiScale(roi_gray)
    eye = eye_cascade.detectMultiScale(roi_gray)

    for (sx, sy, sw, sh) in smile:
        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 1)
    for (sx, sy, sw, sh) in eye:
        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 1)

print(f"Found {len(face_rects)} people.")
cv2.imshow('Image', frame)
cv2.waitKey(0)
