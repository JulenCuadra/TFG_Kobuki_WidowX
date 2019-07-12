#!/usr/bin/env python

import rospy
import serial
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from std_msgs.msg import Float32
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from kobuki_msgs.msg import BumperEvent

info_bumper = 0
orientacion = 0.0
distancia = 0.0
info_temperatura = 0.0

def callback(mensaje):
    global orientacion
    global distancia
    orientacion = mensaje.pose.pose.orientation.z
    distancia = mensaje.pose.pose.position.x

def callback_bumper(mensaje_bumper):
    global info_bumper
    info_bumper = mensaje_bumper.state

def callback_sensor(dato_sensor):
    global info_temperatura
    info_temperatura = dato_sensor.data

def kobuki():
    rospy.init_node('kobuki', anonymous=True)
    sub = rospy.Subscriber('odom', Odometry, callback)
    sub_bumper = rospy.Subscriber('mobile_base/events/bumper', BumperEvent, callback_bumper)
    pub = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)
    velocity_publisher = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size = 10)
    sub_sensor = rospy.Subscriber('datos_sensor2', Float64, callback_sensor)

    rospy.sleep(2)

    trajectory = JointTrajectory()
    trajectory.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "gripper_revolute_joint"]
    trajectory.header.stamp = rospy.Time.now()
    trajectory.header.frame_id = "base_footprint";

    #Pulled back pose
    jtp = JointTrajectoryPoint()
    jtp.positions = [0.0, -0.951, 0.434, 1.502, 0.0, 0.0]
    jtp.time_from_start = rospy.Duration(3)
    trajectory.points.append(jtp)
    #Aproximacion inicial
    jtp_2 = JointTrajectoryPoint()
    jtp_2.positions = [0.0, -0.937, 0.072, 0.853, 0.0, 0.0]
    jtp_2.time_from_start = rospy.Duration(6)
    trajectory.points.append(jtp_2)
    #Aproximacion a la pieza
    jtp_3 = JointTrajectoryPoint()
    jtp_3.positions = [0.0, -0.383, -0.2531, 0.638, 0.0, 0.0]
    jtp_3.time_from_start = rospy.Duration(9)
    trajectory.points.append(jtp_3)

    pub.publish(trajectory)

    rospy.sleep(12)

    if (info_temperatura >= 0.0):

        trajectory_1 = JointTrajectory()
        trajectory_1.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "gripper_revolute_joint"]
        trajectory_1.header.stamp = rospy.Time.now()
        trajectory_1.header.frame_id = "base_footprint";

        #Cierra la pinza
        jtp = JointTrajectoryPoint()
        jtp.positions = [0.0, -0.383, -0.2531, 0.638, 0.0, 1.5]
        jtp.time_from_start = rospy.Duration(3)
        trajectory_1.points.append(jtp)
        #Retroceso
        jtp_1 = JointTrajectoryPoint()
        jtp_1.positions = [0.0, -0.937, 0.072, 0.853, 0.0, 1.5]
        jtp_1.time_from_start = rospy.Duration(6)
        trajectory_1.points.append(jtp_1)
        #Pulled back pose
        jtp_2 = JointTrajectoryPoint()
        jtp_2.positions = [0.0, -0.951, 0.434, 1.502, 0.0, 1.5]
        jtp_2.time_from_start = rospy.Duration(9)
        trajectory_1.points.append(jtp_2)

        pub.publish(trajectory_1)

        tiempo = 0
        tiempo_1 = rospy.Time.now().to_sec()
        while (tiempo <= 12):
            tiempo_2 = rospy.Time.now().to_sec()
            tiempo = tiempo_2-tiempo_1

        vel_msg = Twist()

        vel_msg.linear.x = 0.0
        vel_msg.linear.y = 0.0
        vel_msg.linear.z = 0.0
        vel_msg.angular.x = 0.0
        vel_msg.angular.y = 0.0
        vel_msg.angular.z = 0.5

        while(abs(orientacion) <= 0.999):
            if (info_bumper == 0):
                velocity_publisher.publish(vel_msg)

        vel_msg.angular.z = 0.0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(1)
        vel_msg.linear.x = 0.1
        #t0 = rospy.Time.now().to_sec()
        #current_distance = 0
        while(abs(distancia) <= 1.35):
            if(info_bumper == 0):
                velocity_publisher.publish(vel_msg)
            #t2=rospy.Time.now().to_sec()
            #current_distance= vel_msg.linear.x*(t2-t0)

        vel_msg.linear.x = 0.0
        vel_msg.linear.y = 0.0
        vel_msg.linear.z = 0.0
        vel_msg.angular.x = 0.0
        vel_msg.angular.y = 0.0
        vel_msg.angular.z = 0.0
        velocity_publisher.publish(vel_msg)

        trajectory_2 = JointTrajectory()
        trajectory_2.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "gripper_revolute_joint"]
        trajectory_2.header.stamp = rospy.Time.now()
        trajectory_2.header.frame_id = "base_footprint";
        #Pulled back pose
        jtp = JointTrajectoryPoint()
        jtp.positions = [0.0, -0.951, 0.434, 1.502, 0.0, 1.5]
        jtp.time_from_start = rospy.Duration(3)
        trajectory_2.points.append(jtp)
        #Aproximacion inicial
        jtp_2 = JointTrajectoryPoint()
        jtp_2.positions = [0.0, -0.937, 0.072, 0.853, 0.0, 1.5]
        jtp_2.time_from_start = rospy.Duration(6)
        trajectory_2.points.append(jtp_2)
        #Aproximacion a la pieza
        jtp_3 = JointTrajectoryPoint()
        jtp_3.positions = [0.0, -0.383, -0.2531, 0.638, 0.0, 1.5]
        jtp_3.time_from_start = rospy.Duration(9)
        trajectory_2.points.append(jtp_3)
        #Cierra la pinza
        jtp_4 = JointTrajectoryPoint()
        jtp_4.positions = [0.0, -0.383, -0.2531, 0.638, 0.0, 0.0]
        jtp_4.time_from_start = rospy.Duration(12)
        trajectory_2.points.append(jtp_4)
        #Retroceso
        jtp_5 = JointTrajectoryPoint()
        jtp_5.positions = [0.0, -0.937, 0.072, 0.853, 0.0, 0.0]
        jtp_5.time_from_start = rospy.Duration(15)
        trajectory_2.points.append(jtp_5)
        #Pulled back pose
        jtp_6 = JointTrajectoryPoint()
        jtp_6.positions = [0.0, -0.951, 0.434, 1.502, 0.0, 0.0]
        jtp_6.time_from_start = rospy.Duration(18)
        trajectory_2.points.append(jtp_6)

        pub.publish(trajectory_2)

        tiempo = 0
        tiempo_1 = rospy.Time.now().to_sec()
        while (tiempo <= 20):
            tiempo_2 = rospy.Time.now().to_sec()
            tiempo = tiempo_2-tiempo_1


        vel_msg.linear.x = 0.0
        vel_msg.linear.y = 0.0
        vel_msg.linear.z = 0.0
        vel_msg.angular.x = 0.0
        vel_msg.angular.y = 0.0
        vel_msg.angular.z = 0.5

        while(abs(orientacion) >= 0.01):
            if (info_bumper == 0):
                velocity_publisher.publish(vel_msg)

        vel_msg.angular.z = 0.0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(1)
        vel_msg.linear.x = 0.1
        #t0 = rospy.Time.now().to_sec()
        #current_distance = 0
        while(distancia <= 0.01):
            if(info_bumper == 0):
                velocity_publisher.publish(vel_msg)
            #t2=rospy.Time.now().to_sec()
            #current_distance= vel_msg.linear.x*(t2-t0)

        vel_msg.linear.x = 0.0
        vel_msg.linear.y = 0.0
        vel_msg.linear.z = 0.0
        vel_msg.angular.x = 0.0
        vel_msg.angular.y = 0.0
        vel_msg.angular.z = 0.0
        velocity_publisher.publish(vel_msg)

    else:
        trajectory_3 = JointTrajectory()
        trajectory_3.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "gripper_revolute_joint"]
        trajectory_3.header.stamp = rospy.Time.now()
        trajectory_3.header.frame_id = "base_footprint";

        #Retirada
        jtp = JointTrajectoryPoint()
        jtp.positions = [0.0, -0.937, 0.072, 0.853, 0.0, 0.0]
        jtp.time_from_start = rospy.Duration(3)
        trajectory_3.points.append(jtp)
        #Pulled back pose
        jtp_1 = JointTrajectoryPoint()
        jtp_1.positions = [0.0, -0.951, 0.434, 1.502, 0.0, 0.0]
        jtp_1.time_from_start = rospy.Duration(6)
        trajectory_3.points.append(jtp_1)

        pub.publish(trajectory_3)
        rospy.loginfo("Pieza Fria")
        rospy.sleep(8)


if __name__ == '__main__':
    try:
        kobuki()
    except rospy.ROSInterruptException:
        pass

