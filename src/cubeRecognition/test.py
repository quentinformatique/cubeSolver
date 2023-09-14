import cv2

vid = cv2.VideoCapture(0)


def getColor(hue_value):
    if hue_value < 5:
        return "RED"
    elif hue_value < 22:
        return "ORANGE"
    elif hue_value < 33:
        return "YELLOW"
    elif hue_value < 78:
        return "GREEN"
    elif hue_value < 131:
        return "BLUE"
    elif hue_value < 180:
        return "WHITE"
    else:
        return "Undefined"



while True:
    _, frame = vid.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = width // 2
    cy = height // 2

    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    color = getColor(hue_value)

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    # création d'un tableau sur la camera de 3 lignes et 3 colonnes pour récuperer la couleur dans chaque case, represantant un couleur de 1 piece du ribik's cube
    # 1 2 3
    # 4 5 6
    # 7 8 9

    # ligne 1
    cv2.rectangle(frame, (cx - 220, 130), (cx - 120, 230), (255, 255, 255), 3)
    cv2.rectangle(frame, (cx - 120, 130), (cx - 20, 230), (255, 255, 255), 3)
    cv2.rectangle(frame, (cx - 20, 130), (cx + 80, 230), (255, 255, 255), 3)
    # ligne 2
    cv2.rectangle(frame, (cx - 220, 230), (cx - 120, 330), (255, 255, 255), 3)
    cv2.rectangle(frame, (cx - 120, 230), (cx - 20, 330), (255, 255, 255), 3)
    cv2.rectangle(frame, (cx - 20, 230), (cx + 80, 330), (255, 255, 255), 3)
    # ligne 3
    cv2.rectangle(frame, (cx - 220, 330), (cx - 120, 430), (255, 255, 255), 3)
    cv2.rectangle(frame, (cx - 120, 330), (cx - 20, 430), (255, 255, 255), 3)
    cv2.rectangle(frame, (cx - 20, 330), (cx + 80, 430), (255, 255, 255), 3)

    # quadrillage similaire a celui du dessus mais en plus petit et en bas a gauche de la page

    # ligne 1
    cv2.rectangle(frame, (cx + 120, 130), (cx + 150, 150), (255, 255, 255), 2)
    cv2.rectangle(frame, (cx + 220, 130), (cx + 280, 180), (255, 255, 255), 2)
    cv2.rectangle(frame, (cx + 320, 130), (cx + 420, 230), (255, 255, 255), 2)
    # ligne 2
    cv2.rectangle(frame, (cx + 120, 230), (cx + 220, 330), (255, 255, 255), 2)
    cv2.rectangle(frame, (cx + 220, 230), (cx + 320, 330), (255, 255, 255), 2)
    cv2.rectangle(frame, (cx + 320, 230), (cx + 420, 330), (255, 255, 255), 2)
    # ligne 3
    cv2.rectangle(frame, (cx + 120, 330), (cx + 220, 430), (255, 255, 255), 2)
    cv2.rectangle(frame, (cx + 220, 330), (cx + 320, 430), (255, 255, 255), 2)
    cv2.rectangle(frame, (cx + 320, 330), (cx + 420, 430), (255, 255, 255), 2)



    cv2.imshow("Color", frame)

    key = cv2.waitKey(1)
    if key == 27:  # esc
        break

vid.release()
cv2.destroyAllWindows()
