#!/usr/bin/env python 

import rospy
from dynamic_reconfigure.server import Server
from tune_static_transform.cfg import TuneStaticTFConfig
from geometry_msgs.msg import TransformStamped
import tf2_ros
import tf


if __name__ == "__main__":
    rospy.init_node("tune_static_transform", anonymous = True)

    broadcaster = tf2_ros.StaticTransformBroadcaster()
    static_transformStamped = TransformStamped()

    def callback(config, level):
        global static_transformStamped, broadcaster
        quat = tf.transformations.quaternion_from_euler(
               float(config["pitch"]), float(config["yaw"]), float(config["roll"]))

        static_transformStamped.header.frame_id = config["from"]
        static_transformStamped.child_frame_id = config["to"]

        static_transformStamped.transform.translation.x = float(config["x"])
        static_transformStamped.transform.translation.y = float(config["y"])
        static_transformStamped.transform.translation.z = float(config["z"])

        static_transformStamped.transform.rotation.x = quat[0]
        static_transformStamped.transform.rotation.y = quat[1]
        static_transformStamped.transform.rotation.z = quat[2]
        static_transformStamped.transform.rotation.w = quat[3]

        broadcaster.sendTransform(static_transformStamped)

        return config

    srv = Server(TuneStaticTFConfig, callback)

    rospy.spin()
