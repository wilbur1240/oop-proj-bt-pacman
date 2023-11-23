import rospy
from std_msgs.msg import Float32MultiArray
import numpy as np


class AgentPose_pub():

    scale_pose = []
    last_pose = [0., 0.]

    def __init__(self, topic_pub = 'scale_pose', 
                 topic_sub = 'AgentPose', pub_rate = 100, sub_rate = 10):
        self._pub_topic = topic_pub
        self._sub_topic = topic_sub
        self.pub_rate = pub_rate
        self.sub_rate = sub_rate
        self.pub = rospy.Publisher(self._pub_topic, Float32MultiArray, queue_size=10)
        self.sub = rospy.Subscriber(self._sub_topic, Float32MultiArray, self.callback)

    def publish(self):
        data = self.last_pose
        if len(self.scale_pose) != 0:
            data = self.scale_pose.pop(0)
        self.pub.publish(Float32MultiArray(data=data))

    def callback(self, data):
        diff = data.data - self.last_pose
        for i in range(self.pub_rate/self.sub_rate):
            self.scale_pose.append(self.last_pose + diff * i / (self.pub_rate/self.sub_rate))
        last_pose = data.data

class pacman_pub(AgentPose_pub):
    def __init__(self, topic_pub = 'pacman_scale_pose', 
                 topic_sub = 'pacman_pose', pub_rate = 100, sub_rate = 10):
        super(pacman_pub, self).__init__(topic_pub, topic_sub, pub_rate, sub_rate)

class ghost1_pub(AgentPose_pub):
    def __init__(self, topic_pub = 'ghost1_scale_pose', 
                 topic_sub = 'ghost_blue_pose', pub_rate = 100, sub_rate = 10):
        super(ghost1_pub, self).__init__(topic_pub, topic_sub, pub_rate, sub_rate)

class ghost2_pub(AgentPose_pub):
    def __init__(self, topic_pub = 'ghost2_scale_pose', 
                 topic_sub = 'ghost_orange_pose', pub_rate = 100, sub_rate = 10):
        super(ghost2_pub, self).__init__(topic_pub, topic_sub, pub_rate, sub_rate)


pacman = pacman_pub()
ghost1 = ghost1_pub()
ghost2 = ghost2_pub()

    

def main():
    rospy.init_node('Agent_scale_pose', anonymous=True)
    r = rospy.Rate(100) # 10hz 
    while not rospy.is_shutdown():
        pacman.publish()
        ghost1.publish()
        ghost2.publish()
        r.sleep()


if __name__ == '__main__':
    main()