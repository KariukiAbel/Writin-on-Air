import cv2
import numpy as np

#to install opencv, have good internet and copy this: pip install opencv-python and for numpy do pip install numpy

###global###
x,y,k = 200, 200, -1

cap = cv2.VideoCapture(0)

def take_inp(event, x1, y1, flag, param):
    global x,y,k
    if event == cv2.EVENT_LBUTTONDOWN:
        x = x1
        y = y1
        k = 1
        
cv2.namedWindow("Enter_point")
cv2.setMouseCallback("Enter_point", take_inp)

#taking input point
while True:
    
    _, inp_img = cap.read()
    inp_img = cv2.flip(inp_img, 1)
    gray_inp_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Enter_point", inp_img)
    
    if k == 1 or cv2.waitKey(30) == 27:
        cv2.destroyAllWindows()
        break
    
stp = 0

