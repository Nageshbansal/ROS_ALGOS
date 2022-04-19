#! /usr/bin/env python3 
import rospy
from std_msgs.msg import Float64

def motor_vel(speed,flag):
    pub = rospy.Publisher(
        ''
    )