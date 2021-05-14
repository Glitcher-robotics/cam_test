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

bridge = CvBridge()

def cam_callback(imgmsg):
    img = bridge.imgmsg_to_cv2(imgmsg, 'rgb8')
    # img = imgmsg.bridge.imgmsg_to_cv2('bgr8')
    # img = cv2.imread(img_raw)
    print(img)
    # cv2.imwrite('test.png', img)
    cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
    cv2.imshow('demo', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        rospy.signal_shutdown('quit')
    

def listen():
    rospy.init_node('cam_sub')
    rospy.Subscriber("/camera/image_raw", Image, cam_callback)
    rospy.spin()

while not rospy.is_shutdown():
    listen()

