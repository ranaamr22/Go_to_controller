#!/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time 
from std_srvs.srv import Empty
x=0
y=0
z=0
yaw=0
rospy.init_node('turtlesim_motion_pose' ,anonymous=True)

def poseCallback(pose_message):
    global x
    global y,z,yaw
    x= pose_message.x
    y= pose_message.y
    yaw = pose_message.theta

def go_to_goal(x_goal,y_goal):
    global x
    global y, z, yaw
    velocity_message = Twist()
   
    cmd_vel_topic = "/turtle1/cmd_vel"  
    velocity_publisher = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)

    while not rospy.is_shutdown():
        k_linear = 0.5
        distance = math.sqrt(((x_goal-x) ** 2)+((y_goal-y) ** 2))
        linear_speed = distance * k_linear

        k_angular = 4.0
        desired_angle_goal = math.atan2(y_goal-y ,x_goal-x)
        angular_speed = (desired_angle_goal - yaw )*k_angular

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed

        velocity_publisher.publish(velocity_message)

        if (distance < 0.01):
            
            print ('x=', x ,'y=',y)
            break

rospy.Subscriber("/turtle1/pose",Pose ,poseCallback)
go_to_goal(3, 8)

        
        