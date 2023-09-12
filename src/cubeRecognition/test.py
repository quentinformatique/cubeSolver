import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while True:
    _, frame = vid.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = width // 2
    cy = height // 2

    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 180:
        color = "WHITE"


    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    cv2.imshow("Color", frame)


    key = cv2.waitKey(1)
    if key == 27: # esc
        break

vid.release()
cv2.destroyAllWindows()
