import numpy as np
import cv2

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

position=[0,0]

def on_mouse_click(event, x,y, flags, param):
    if event==cv2.EVENT_FLAG_LBUTTON:
        global position
        position=[y,x]

cv2.setMouseCallback("Image", on_mouse_click)

cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_AUTO_EXPOSURE,1)
cam.set(cv2.CAP_PROP_EXPOSURE,-4)
cam.set(cv2.CAP_PROP_AUTO_WB,0)


#101-102,190-195,172-174
lower=np.array([65,184,118])
upper=np.array([110,255,255])

while cam.isOpened():
    _,frame=cam.read()
    frame=cv2.GaussianBlur(frame,(21,21), 0)
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower,upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours)>0:
        c=max(contours, key=cv2.contourArea)
        (x,y),radius=cv2.minEnclosingCircle(c)
        if radius>20:
            cv2.circle(frame, (int(x),int(y)), int(radius),(0,255,255),0)

    cv2.imshow("Image",frame)
    key=cv2.waitKey(50)
    if key == ord('q'):
        break
    
cv2.destroyAllWindows()
