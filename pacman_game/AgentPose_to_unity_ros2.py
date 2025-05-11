#!/usr/bin/env python3

import rclpy
from std_msgs.msg import Float32MultiArray
import numpy as np
import time

PUBLISH_RATE = 100  # Hz

class AgentPosePub:
    def __init__(self, node, topic_pub, topic_sub):
        self.node = node
        self.scale_pose = []
        self.last_pose = np.array([0.0, 0.0])

        self.pub = node.create_publisher(Float32MultiArray, topic_pub, 10)
        self.sub = node.create_subscription(Float32MultiArray, topic_sub, self.callback, 10)

    def publish(self):
        data = self.last_pose
        if self.scale_pose:
            data = self.scale_pose.pop(0)
        msg = Float32MultiArray(data=list(data))
        self.pub.publish(msg)

    def callback(self, msg):
        x, y = msg.data
        self.last_pose = np.array([x, y])

# ----- You should define the class for each agent in this area ----- #

class Pacman_Pub():


class Ghost1_Pub():


class Ghost2_Pub():


# ----- And don't forget to define class objects ----- #

def main():
    rclpy.init()
    node = rclpy.create_node('agent_scale_pose')



    publish_period = 1.0 / PUBLISH_RATE

    try:
        while rclpy.ok():
            pacman.publish()
            ghost1.publish()
            ghost2.publish()

            # Process incoming messages
            rclpy.spin_once(node, timeout_sec=0.0)
            time.sleep(publish_period)

    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
# --- Call the main function here --- #

# ----------------------------------- #
