#!/usr/bin/env bash

REPOSITORY="wilbur1240/oop"
TAG="ros2-unity"

IMG="${REPOSITORY}:${TAG}"

docker pull "${IMG}"
