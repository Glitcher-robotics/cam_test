import numpy as np
import cv2

print(cv2.getBuildInformation())

def open_mipi(width, height):
    gst_str = ('nvarguscamerasrc !'
               'video/x-raw(memory:NVMM), '
               'width=(int)2592, height=(int)1458, '
               'format=(string)NV12, framerate=(fraction)30/1 ! '
               'nvvidconv ! '
               'video/x-raw, width=(int){}, height=(int){}, '
               'format=(string)BGRx ! '
               'videoconvert ! appsink').format(width, height)
    return cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

width = 640
height = 360



cap = open_mipi(width, height)

if not cap.isOpened():
   print('Failed to open camera')
   

while(True):
    ret, frame = cap.read()



########################################################################
    # add filtering codes
    
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)


########################################################################
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
