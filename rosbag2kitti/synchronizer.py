import roslib;  
import rosbag
import rospy
import message_filters
from sensor_msgs.msg import Image# the data type you want to synchronize  | 要同步的数据类型
from nav_msgs.msg import Odometry# the data type you want to synchronize | 要同步的数据类型
import sys
from std_msgs.msg import Int32, String

bag = rosbag.Bag('test.bag', 'w')#create a new bag you want to write the synchronized messages into |新bag的名字
class sync_listener:
		def __init__(self):
						self.image_sub = message_filters.Subscriber('/camera/image_raw', Image)# the topic you want to synchronize | 要同步的话题 
						self.info_sub = message_filters.Subscriber('/lvi_sam/lidar/mapping/odometry', Odometry)# the topic you want to synchronize | 要同步的话题
						self.ts = message_filters.ApproximateTimeSynchronizer([self.image_sub, self.info_sub], 10,0.1) 
						self.ts.registerCallback(self.callback)
		def callback(self, image, odometry):
						print("done")
						try:
							bag.write('image', image) # the topic name of your new bag | 新bag的话题名
							bag.write('odometry', odometry)	 # the topic name of your new bag | 新bag的话题名			
						except Exception as e:
							print(e)				
							

def main(args):
		sl = sync_listener()
		rospy.init_node('sample_message_filters', anonymous=True)
		try:
			rospy.spin()
		except KeyboardInterrupt:
			print("Shutting down")
		finally:
			bag.close()

if __name__ == '__main__':
    main(sys.argv)
    
