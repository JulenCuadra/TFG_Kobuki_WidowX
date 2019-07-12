#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

def home_default():
    rospy.sleep(5) ##Esperamos hasta que el resto de nodos esten activos al invocarlos con roslaunch.
    pub = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10) 
    rospy.init_node('home_default', anonymous=True)
    rospy.loginfo("Going Home")

    trajectory = JointTrajectory()
    trajectory.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "gripper_revolute_joint"]
    trajectory.header.stamp = rospy.Time.now()
    trajectory.header.frame_id = "base_footprint";
    
    jtp = JointTrajectoryPoint()
    jtp.positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    jtp.velocities = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    jtp.time_from_start = rospy.Duration(3)
    trajectory.points.append(jtp)

    pub.publish(trajectory)


if __name__ == '__main__':
    home_default()

