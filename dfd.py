import cv2
import numpy as np
from random import randint

win = False

def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global position
        print(position)
        position = [y, x]

def make_random_sequence():
    ar = [randint(0, 2), randint(0, 1), 3]
    if (ar[1] > 0):
        ar[1] = (ar[0] + 1) % 3
    else:
        ar[1] = (ar[0] - 1) % 3
    ar[2] = ar[2] - ar[1] - ar[0]
    return ar

def check_for_win(array, sequence):
    x = len(array)
    if (x > 2):
        if (array[x - 1][0] == sequence[2] and
            array[x - 2][0] == sequence[1] and
            array[x - 3][0] == sequence[0]):
            color = ["YELLOW", "ORANGE", "RED"]
            print("You win! Your sequence:", color[array[x - 3][0]], color[array[x - 2][0]], color[array[x - 1][0]],
                  "Expected:", color[sequence[0]], color[sequence[1]], color[sequence[2]])
            global win
            win = True  # yeah I know it's bad but doesn't seem really matter rn

def compare(ball):
    return ball[1]


cam = cv2.VideoCapture(0)
cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)
cv2.setMouseCallback("Camera", on_mouse_click)
position = []
measures = []
bgr_color = []
hsv_color = []

yellow_lower_HSV = np.array([23, 52, 106])
yellow_upper_HSV = np.array([30, 255, 215])
orange_lower_HSV = np.array([3, 80, 176])
orange_upper_HSV = np.array([5, 255, 250])
red_lower_HSV = np.array([0, 52, 76])
red_upper_HSV = np.array([0, 255, 255])

sequence = make_random_sequence()

while cam.isOpened():
    _, image = cam.read()
    blurred = cv2.GaussianBlur(image, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    masks = [cv2.inRange(hsv, yellow_lower_HSV, yellow_upper_HSV), 
             cv2.inRange(hsv, orange_lower_HSV, orange_upper_HSV),
             cv2.inRange(hsv, red_lower_HSV, red_upper_HSV)]
    cntss = []
    user = []
    for i in range(len(masks)):
        masks[i] = cv2.erode(masks[i], None, iterations=2)
        masks[i] = cv2.dilate(masks[i], None, iterations=2)
        cntss.append(cv2.findContours(masks[i].copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2])
        if (len(cntss[i]) > 0):
            c = max(cntss[i], key=cv2.contourArea)
            [curr_x, curr_y], radius = cv2.minEnclosingCircle(c)
            if (radius > 10):
                cv2.circle(image, (int(curr_x), int(curr_y)), 5, (0, 255, 255,), 2)
                #cv2.circle(image, (int(curr_x), int(curr_y)), int(radius), (0, 255, 255,), 2)
                user.append([i, curr_x])
        if (len(user) == 3):
            user = sorted(user, key=compare)
            if (win == False):
                check_for_win(user, sequence)

    if position:
        pxl = image[position[0], position[1]]
        measures.append(pxl)
        if len(measures) >= 10:
            bgr_color = np.uint8([[np.average(measures, 0)]])
            hsv_color = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)
            bgr_color = bgr_color[0, 0]
            hsv_color = hsv_color[0, 0]
            measures.clear()
        cv2.circle(image, (position[1], position[0]), 7, (255, 127, 255), 3)
    cv2.putText(image, f"Color BGR = {bgr_color}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(image, f"Color HSV = {hsv_color}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.imshow("Camera", image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
