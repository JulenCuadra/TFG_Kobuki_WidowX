#!/usr/bin/env python

import rospy
import serial
from std_msgs.msg import String
from std_msgs.msg import Float64


def lector_sensor2():
    serial_conn = None
    for i in range(0,5):
        serial_port = "/dev/ttyUSB" + str(i)
    	try:
	    serial_conn = serial.Serial(serial_port)
            break
        except:
	    continue

    pub = rospy.Publisher('datos_sensor2', Float64, queue_size=10)
    rospy.init_node('lector_sensor2')
    while not rospy.is_shutdown():
        dato = serial_conn.readline()
        rospy.loginfo("-->Lector_Sensor2: " + dato)
        pub.publish(float(dato))


if __name__ == '__main__':
    lector_sensor2()

