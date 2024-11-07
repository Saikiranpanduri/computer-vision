import cv2
import numpy as np
cap = cv2.VideoCapture("C:/Users/pandu/Videos/Screen Recordings/Screen Recording 2024-11-07 140026.mp4")
if(cap.isOpened()==False):
    print("Error ")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame',frame)
        if(cv2.waitKey(250)& 0xFF == ord('q')):
           break
    else:
        break
cap.release()
cv2.destroyAllWindows()
