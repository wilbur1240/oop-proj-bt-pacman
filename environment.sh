#!/bin/bash

source /opt/ros/humble/setup.bash
source ./ros2_ws/install/setup.bash  # Uncomment if needed

if [ "$1" ]; then
    echo "Setting ROS 2 Domain ID to $1"
    export ROS_DOMAIN_ID=$1
else
    echo "ROS_DOMAIN_ID not set, using default (0)"
    export ROS_DOMAIN_ID=0
fi

if [ "$2" ]; then
    echo "Setting ROS 2 IP to $2"
    export ROS_IP=$2
    export ROS_HOSTNAME=$2
else
    echo "ROS_IP not set, using localhost"
    export ROS_IP=127.0.0.1
    export ROS_HOSTNAME=localhost
fi

# Optional: avoid localhost-only communication
export ROS_LOCALHOST_ONLY=1

echo "ROS 2 environment configured."
