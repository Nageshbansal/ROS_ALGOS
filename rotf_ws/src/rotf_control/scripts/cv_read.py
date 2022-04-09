#!/usr/bin/env python3
from __future__ import print_function

import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("image_topic_2",Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/color/image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image.shape
    img_heigth = rows
    img_width = cols/4
    # print(img_heigth,img_width)

    # img = np.zeros(img_width , img_heigth, 2)
    img_1 = np.reshape(cv_image[:,0:160,:],(img_heigth,img_width,3))
    img_2 = np.reshape(cv_image[:,160:320,:],(img_heigth,img_width,3))
    img_3 = np.reshape(cv_image[:,320:480,:],(img_heigth,img_width,3))
    img_4 = np.reshape(cv_image[:,480:640,:],(img_heigth,img_width,3))
    
    print(np.shape(img_1),np.shape(img_2),np.shape(img_3),np.shape(img_4))
    cv2.imshow("Image window", cv_image)
    cv2.imshow("Image_1 window", img_1)
    cv2.imshow("Image_2 window", img_2)
    cv2.imshow("Image_3 window", img_3)
    cv2.imshow("Image_4 window", img_4)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
