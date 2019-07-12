#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint



def trayectoria_2():
    
    pub = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10) 
    rospy.init_node('trayectoria_2', anonymous=True)

    trajectory = JointTrajectory()
    trajectory.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "gripper_revolute_joint"]
    trajectory.header.stamp = rospy.Time.now()
    trajectory.header.frame_id = "base_footprint";
    #Posicion default
    jtp = JointTrajectoryPoint()
    jtp.positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    jtp.velocities = [0.1, 0.1, 0.1, 0.1, 0.0, 0.0]
    jtp.time_from_start = rospy.Duration(3)
    trajectory.points.append(jtp)
    #Aproximacion a la pieza
    jtp_2 = JointTrajectoryPoint()
    jtp_2.positions = [0.0, 0.8560, 0.5522, -1.3622, 0.0, 0.0]
    jtp_2.velocities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    jtp_2.time_from_start = rospy.Duration(6)
    trajectory.points.append(jtp_2)
    #Cierra la pinza
    jtp_3 = JointTrajectoryPoint()
    jtp_3.positions = [0.0, 0.8560, 0.5522, -1.3622, 0.0, 1.5]
    jtp_3.velocities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    jtp_3.time_from_start = rospy.Duration(9)
    trajectory.points.append(jtp_3)
    #Sube
    jtp_4 = JointTrajectoryPoint()
    jtp_4.positions = [0.0, -0.2362, -0.5844, 0.4488, 0.0, 1.5]
    jtp_4.velocities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    jtp_4.time_from_start = rospy.Duration(12)
    trajectory.points.append(jtp_4)
    #Giro del brazo
    jtp_5 = JointTrajectoryPoint()
    jtp_5.positions = [1.6, -0.2362, -0.5844, 0.4488, 0.0, 1.5]
    jtp_5.velocities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    jtp_5.time_from_start = rospy.Duration(15)
    trajectory.points.append(jtp_5)
    #Aproximacion a destino
    jtp_6 = JointTrajectoryPoint()
    jtp_6.positions = [1.6, -0.1212, -0.8375, 0.9741, 0.0, 1.5]
    jtp_6.velocities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    jtp_6.time_from_start = rospy.Duration(18)
    trajectory.points.append(jtp_6)
    #Suelta la pieza
    jtp_7 = JointTrajectoryPoint()
    jtp_7.positions = [1.6, -0.1212, -0.8375, 0.9741, 0.0, 0.0]
    jtp_7.velocities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    jtp_7.time_from_start = rospy.Duration(21)
    trajectory.points.append(jtp_7)
    #Gira de vuelta
    jtp_8 = JointTrajectoryPoint()
    jtp_8.positions = [0.0, -0.1212, -0.8375, 0.9741, 0.0, 0.0]
    jtp_8.velocities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    jtp_8.time_from_start = rospy.Duration(24)
    trajectory.points.append(jtp_8)
    #Posicion default
    jtp_9 = JointTrajectoryPoint()
    jtp_9.positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    jtp_9.velocities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    jtp_9.time_from_start = rospy.Duration(27)
    trajectory.points.append(jtp_9)    

    pub.publish(trajectory)


if __name__ == '__main__':
    try:
        trayectoria_2()
    except rospy.ROSInterruptException():
        pass
