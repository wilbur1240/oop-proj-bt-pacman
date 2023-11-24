# Pacman with Publisher to Unity
This script will tell you how to run and publish data to unity.
## How to run
First terminal: \
Start the roscore and rosbridge for translating data.
```
source docker_run.sh
source environment.sh
roslaunch rosbridge_server rosbridge_websocket.launch
```
Second terminal: \
Initiate the Pacman game locally. \
And publish three agents' discrete position. \
> topic name:
    /pacman_pose
    /ghost_blue_pose
    /ghost_orange_pose
> msgs type: 
    Float32MultiArray
```
source docker_join.sh
source environment.sh
cd pacman_game
python3 pacmen.py
```
Third terminal: \
You can decide whether to run this task or not, as it will publish the continuous positions of three agents.
> topic name:
    /pacman_scale_pose
    /ghost1_scale_pose
    /ghost2_scale_pose
> msgs type: 
    Float32MultiArray
```
source docker_join.sh
source environment.sh
cd pacman_game
python3 AgentPose_to_unity.py
```