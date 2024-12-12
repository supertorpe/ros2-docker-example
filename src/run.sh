#!/bin/bash

cd /ros2/ws
source /opt/ros/jazzy/setup.bash
source /ros2/ws/install/setup.bash
ros2 daemon start
ros2 run pkg_foo node_bar
