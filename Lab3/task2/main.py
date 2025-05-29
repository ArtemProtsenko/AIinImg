import cv2
import numpy as np


def process_image(img):
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel_size = 5
    blur = cv2.GaussianBlur(grayscale, (kernel_size, kernel_size), 0)

    low_t = 50
    high_t = 150
    edges = cv2.Canny(blur, low_t, high_t)

    vertices = np.array([
        [(0, img.shape[0]),
         (550, 400), (650, 400),
         (img.shape[1], img.shape[0])]
    ], dtype=np.int32)
    mask = np.zeros_like(edges)
    ignore_mask_color = 255
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_edges = cv2.bitwise_and(edges, mask)

    def draw_lines(img, lines, color=[255, 0, 0], thickness=7):
        x_bottom_pos = []
        x_upper_pos = []
        x_bottom_neg = []
        x_upper_neg = []

        y_bottom = 720
        y_upper = 400

        for line in lines:
            for x1, y1, x2, y2 in line:
                if x2 == x1:
                    continue  # уникаємо ділення на нуль
                slope = (y2 - y1) / (x2 - x1)

                if 0.3 < slope < 1:
                    b = y1 - slope * x1
                    x_bottom_pos.append((y_bottom - b) / slope)
                    x_upper_pos.append((y_upper - b) / slope)
                elif -1 < slope < -0.3:
                    b = y1 - slope * x1
                    x_bottom_neg.append((y_bottom - b) / slope)
                    x_upper_neg.append((y_upper - b) / slope)

        lines_mean = []
        if x_bottom_pos and x_upper_pos:
            lines_mean.append([
                int(np.mean(x_bottom_pos)), y_bottom,
                int(np.mean(x_upper_pos)), y_upper
            ])
        if x_bottom_neg and x_upper_neg:
            lines_mean.append([
                int(np.mean(x_bottom_neg)), y_bottom,
                int(np.mean(x_upper_neg)), y_upper
            ])

        for line in lines_mean:
            cv2.line(img, (line[0], line[1]), (line[2], line[3]), color, thickness)

    rho = 3
    theta = np.pi / 180
    threshold = 15
    min_line_length = 150
    max_line_gap = 60
    lines = cv2.HoughLinesP(
        masked_edges, rho, theta, threshold,
        np.array([]),
        minLineLength=min_line_length,
        maxLineGap=max_line_gap)

    if lines is not None:
        draw_lines(img, lines)


video_capture = cv2.VideoCapture("vid.mp4")

while video_capture.isOpened():
    ret, frame = video_capture.read()
    if ret:
        process_image(frame)
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

video_capture.release()
cv2.destroyAllWindows()
