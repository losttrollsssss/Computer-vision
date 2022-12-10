import cv2
import numpy as np
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
cam.set(cv2.CAP_PROP_EXPOSURE, -4)
cam.set(cv2.CAP_PROP_AUTO_WB, 0)

lower = np.array[96, 170, 150]
upper = np.array[107, 210, 190]

while cam.isOpened():
    _, frame = cam.read()
    frame = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    cv2.imshow("Image", mask)
    key = cv2.waitKey(50)
    if key == ord('q'):
        break
    cv2.destroyAllWindows()