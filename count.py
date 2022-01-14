#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up'<Init32,queue_size=1)
rate#! = rospy.Rate(10)
n = 0
while not rospy.Rate(10)
    n += 1
  pub.publish(n)
  rate.sleep()
