#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import sys
import cv2
import gi
import numpy as np
from cv_bridge import CvBridge
gi.require_version('Gst', '1.0')
from gi.repository import Gst


class Camera:
    def __init__(self):
        self.pub = rospy.Publisher("/camera_test/images", Image, queue_size=1)
        self.cvb = CvBridge()

    def read_cam(self):
        # cap = cv2.VideoCapture(0)
        gst_str = ( 'nvarguscamerasrc !'
                    'nvvidconv !'
                    'video/x-raw(memory:NVMM), '
                    'width=(int)2592, height=(int)1458, '
                    'format=(string)I420, framerate=(fraction)30/1 ! '
                    'nvvidconv ! '
                    'video/x-raw, width=(int){}, height=(int){}, '
                    'format=(string)BGRx ! '
                    'videoconvert ! appsink').format(640, 360)
        cap = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)
        if cap.isOpened():
            print("cap is opened but")
            cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
            while not rospy.core.is_shutdown():
                ret_val, img = cap.read()
                print(type(img), ret_val,)
                self.pub.publish(self.cvb.cv2_to_imgmsg(img, 'bgr8'))
                cv2.imshow('demo',img)
                if cv2.waitKey(1) == ord('q'):
                    break
        else:
            print("Cap failed")


if __name__=="__main__":
    cam = Camera()
    rospy.init_node('camera')
    try:
        cam.read_cam()
        rospy.spin()
        outcome = 'Test Completed'
    except rospy.ROSInterruptException:
        print("Exception")
        pass
    rospy.core.signal_shutdown(outcome)