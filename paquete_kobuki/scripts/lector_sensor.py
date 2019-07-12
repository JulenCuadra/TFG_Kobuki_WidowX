#!/usr/bin/env python

import rospy
import serial
from std_msgs.msg import String
from std_msgs.msg import Float64
import time

def lector_sensor2():
    serial_conn = serial.Serial("/dev/ttyUSB0")

    pub = rospy.Publisher('datos_sensor2', Float64, queue_size=10)
    rospy.init_node('lector_sensor2')
    while not rospy.is_shutdown():
        try:
            dato = serial_conn.readline()
            dato_withoutCRLF = dato.replace("\r","").replace("\n", "")
            rospy.loginfo("--> Received from serial port: " + dato_withoutCRLF)
            data_array = dato_withoutCRLF.split("#")
            for each in data_array:
                if each:
                    rospy.loginfo("---> Publishing to /datos_sensor2: " + each)
	            pub.publish(float(dato_cleaned))
        except:
            pass


if __name__ == '__main__':
    lector_sensor2()

