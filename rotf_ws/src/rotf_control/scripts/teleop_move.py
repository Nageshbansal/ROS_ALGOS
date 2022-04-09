import rospy
from geometry_msgs.msg import Twist
from rospy.core import is_shutdown

rospy.init_node('teleop_move')
rate = rospy.Rate(100)
move=Twist()
move.linear.x=10
move.angular.z=0.0
# def move_bot(msg):
#     global v_x
#     if msg == 'w':
#         v_x += 10
#     elif msg == 's':
#         v_x = 0

#     return v_x , v_y



pub = rospy.Publisher("/cmd_vel",Twist,queue_size=1)

while not rospy.is_shutdown():
    # msg = input("enter w or s")
    # v_x , v_y = move_bot(msg)
    v_x = 100
    pub.publish(move)
    rospy.sleep()