'''
capture_frame.py
'''

# import modules
import cv2
import numpy
import sys

cap = cv2.VideoCapture(0)
ret, img = cap.read()
cv2.imshow("Image", img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    sys.exit()



