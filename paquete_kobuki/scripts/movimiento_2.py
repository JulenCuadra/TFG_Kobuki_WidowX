#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

def movimiento_2():

    rospy.init_node('movimiento_2', anonymous=True)
    velocity_publisher = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size = 10)
    vel_msg = Twist()

    vel_msg.linear.x = 0.1
    vel_msg.linear.y = 0.0
    vel_msg.linear.z = 0.0
    vel_msg.angular.x = 0.0
    vel_msg.angular.y = 0.0
    vel_msg.angular.z = 0.0


    t0 = rospy.Time.now().to_sec()
    current_distance = 0

    while(current_distance <= 1):

        velocity_publisher.publish(vel_msg)
        t1=rospy.Time.now().to_sec()
        current_distance= vel_msg.linear.x*(t1-t0)

    vel_msg.linear.x = 0.0
    #velocity_publisher.publish(vel_msg)
    #rospy.sleep(1)
    vel_msg.angular.z = 0.5
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle <= 3.85):

        velocity_publisher.publish(vel_msg)
        t2=rospy.Time.now().to_sec()
        current_angle= vel_msg.angular.z*(t2-t0)

    vel_msg.linear.x = 0.0
    vel_msg.linear.y = 0.0
    vel_msg.linear.z = 0.0
    vel_msg.angular.x = 0.0
    vel_msg.angular.y = 0.0
    vel_msg.angular.z = 0.0
    velocity_publisher.publish(vel_msg)
    rospy.sleep(1)
    vel_msg.linear.x = 0.1
    t0 = rospy.Time.now().to_sec()
    current_distance = 0

    while(current_distance <= 1):

        velocity_publisher.publish(vel_msg)
        t3=rospy.Time.now().to_sec()
        current_distance= vel_msg.linear.x*(t3-t0)

    vel_msg.linear.x = 0.0
    #velocity_publisher.publish(vel_msg)
    #rospy.sleep(1)
    vel_msg.angular.z = 0.5
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle <= 3.85):

        velocity_publisher.publish(vel_msg)
        t4=rospy.Time.now().to_sec()
        current_angle= vel_msg.angular.z*(t4-t0)



    vel_msg.angular.z = 0.0

    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    movimiento_2()

