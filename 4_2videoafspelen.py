# Bron: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
# Met aanpassing op regel 7 (bestandsnaam) 

import numpy as np
import cv2 as cv
 
cap = cv.VideoCapture('filename.avi') # Bestand gegenereerd door 3_2webcamvideo.py
 
while cap.isOpened():
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
 
cap.release()
cv.destroyAllWindows()
