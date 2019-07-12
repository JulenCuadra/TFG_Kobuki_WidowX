#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint



def trayectoria_definitiva1():
    
    pub = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10) 
    rospy.init_node('trayectoria_definitiva1', anonymous=True)

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
    #Cierra la pinza
    jtp_4 = JointTrajectoryPoint()
    jtp_4.positions = [0.0, -0.383, -0.2531, 0.638, 0.0, 1.7]
    jtp_4.time_from_start = rospy.Duration(12)
    trajectory.points.append(jtp_4)
    #Retroceso
    jtp_5 = JointTrajectoryPoint()
    jtp_5.positions = [0.0, -0.937, 0.072, 0.853, 0.0, 1.7]
    jtp_5.time_from_start = rospy.Duration(15)
    trajectory.points.append(jtp_5)
    #Pulled back pose
    jtp_6 = JointTrajectoryPoint()
    jtp_6.positions = [0.0, -0.951, 0.434, 1.502, 0.0, 1.7]
    jtp_6.time_from_start = rospy.Duration(18)
    trajectory.points.append(jtp_6)   

    pub.publish(trajectory)
    
if __name__ == '__main__':
    try:
        trayectoria_definitiva1()
    except rospy.ROSInterruptException:
        pass
    

