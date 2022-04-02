
#coding:utf-8

import roslib;  
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
import os
path='/home/star/fisheyeakittiData/pic/' #the path of the directory you want to save images , absolute path |  要存储图片的文件夹路径
counter = 0
first_frame_time=0
class ImageCreator():


    def __init__(self):
        self.bridge = CvBridge()
        with rosbag.Bag('test.bag', 'r') as bag:   #The name of the bag you want to read | 要读取的bag名
            for topic,msg,t in bag.read_messages():
                if topic == "image":  #image topic
                        try:
                            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                        except CvBridgeError as e:
                            print (e)
                        global counter
                        global first_frame_time
                        if counter==0:
                            first_frame_time=msg.header.stamp.to_sec()
                        counter= counter+1
                        #name images with their timestamps | 以时间戳命名图片
                         #retain 6 decimal places , can be modified according to the accuracy | 小数点后带有6位，可根据精确度需要修改
                        timestr = "%.6f" %  msg.header.stamp.to_sec()
                        image_name = timestr+ ".png"
                        #save
                        cv2.imwrite(path+image_name, cv_image)  
                        #output to the times.txt files
                        with open('times.txt','a') as file:
                                #minus the timestamp of the first frame, use relative time|减去第一帧的时间戳，使用相对时间
                                file.write(str("{:e}".format(msg.header.stamp.to_sec()-first_frame_time)))
                                file.write("\r")
        # rename .png files using kitti format | 以kitti形式重命名.png文件
        filelist = os.listdir(path)
        #make it traverse files in order | 按顺序遍历图片
        filelist.sort()
        i = 0
        for item in filelist:
                # print('item name is ',item)
                if item.endswith('.png'):
                        i = i + 1
                        # convert numbers to strings
                        # the first image is named as 000001.png , add leading zeros to the number i.(6 digits)
                        name = str(i).rjust(6,'0')
                        # the path of original images
                        src = os.path.join(os.path.abspath(path),item)
                        # the path of destination images
                        dst = os.path.join(os.path.abspath(path),name + '.png')
                try:
                        os.rename(src,dst)
                        # print the conversion results for checking | 将转换结果在终端打印出来以便检查
                        print('rename from %s to %s'%(src,dst))
                except:
                        continue

if __name__ == '__main__':

    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
