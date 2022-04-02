#coding:utf-8

import roslib;  
import rosbag
import rospy
from geometry_msgs.msg import Pose
import numpy as np
from quaternion2rotation import *


counter = 0
class OdometryChecker():
	
	def __init__(self):
		with rosbag.Bag('test.bag', 'r') as bag:   #the name of the bag you want to read
		    for topic,msg,t in bag.read_messages():
							if topic == "odometry":  
								rospy.sleep(1)
								curr_time = msg.header.stamp
								global counter
								counter= counter+1
								print (counter, curr_time)
								print
								pose = msg.pose.pose #  the x,y,z pose and quaternion orientation
								#print (pose.position.x)
								R=quaternion_rotation_matrix([pose.orientation.x,pose.orientation.y,pose.orientation.z,pose.orientation.w])
								t=np.array([[pose.position.x,pose.position.y,pose.position.z]]).T
								Rt = np.concatenate([R,t], axis=-1) # [R|t]
								print(Rt)
								#output to the poses.txt files
								with open('poses.txt','a') as file:
									for r in Rt:
										for c in r:
											file.write(str("{:e}".format(c))+" ")
									file.write("\r")
							

			    

if __name__ == '__main__':

    try:
        odometry_checker = OdometryChecker()
    except rospy.ROSInterruptException:
        pass


