#!/usr/bin/env python

from os import name
import roslib
from rospy.timer import Rate
roslib.load_manifest('learning_tf')
import rospy
import tf
import math

if __name__ == "__main__":
    rospy.init_node('dynamic_tf_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        t = rospy.Time.now().to_sec() * math.pi
        br.sendTransform((0,2.0*math.cos(t),0.0),
                        (0.0,0.0,0.0,1.0),
                        rospy.Time.now(),
                        "carrot1",
                        "turtle1")
        rate.sleep()
