#!/bin/bash

source /opt/ros/jazzy/setup.bash
cd /ros2/ws
/ros2/venv/bin/python3 -m pip install -r src/pkg_foo/requirements.txt
colcon build --packages-select pkg_foo
