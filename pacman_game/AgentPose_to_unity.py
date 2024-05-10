import rospy
from std_msgs.msg import Float32MultiArray
import numpy as np


PUBLISH_RATE = 100
SUBSCRIBE_RATE = 10

class AgentPose_pub():

    scale_pose = []
    last_pose = np.array([0., 0.])

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
        x, y = data.data
        pose = np.array([x, y])
        if self.last_pose[0] != pose[0] and self.last_pose[1] != pose[1]:
            diff = pose - np.array(self.last_pose)
            # print(diff)
            for i in range(int(self.pub_rate/self.sub_rate)):
                tmp = self.last_pose + diff * i / int(self.pub_rate/self.sub_rate)
                self.scale_pose.append([tmp[0], tmp[1]])
            self.last_pose = np.array([x, y])


# ----- You should define the class for each agent in this area ----- #

class pacman_pub():


class ghost1_pub():


class ghost2_pub():


# ----- And don't forget to define variables ----- #
    

def main():
    rospy.init_node('Agent_scale_pose', anonymous=False)
    r = rospy.Rate(PUBLISH_RATE) # 100hz 
    while not rospy.is_shutdown():
        pacman.publish()
        ghost1.publish()
        ghost2.publish()
        r.sleep()


if __name__ == '__main__':

# --- Call the main function here --- #

# ----------------------------------- #