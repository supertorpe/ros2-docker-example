FROM osrf/ros:jazzy-desktop

ENV RUFF_CACHE_DIR=/tmp/.ruff_cache
ENV MYPY_CACHE_DIR=/tmp/.mypy_cache
ENV PYTHONPATH=/usr/lib/python3/dist-packages:/ros2/ws/install/pkg_foo/lib/python3.12/site-packages:/opt/ros/jazzy/lib/python3.12/site-packages:/ros2/venv/lib/python3.12/site-packages

RUN apt update && apt -y upgrade &&\
    apt -y install python3-pip virtualenv cython3 &&\
    mkdir -p /ros2/ws /ros2/venv &&\
    virtualenv -p python3 /ros2/venv/ &&\
    touch /ros2/venv/COLCON_IGNORE &&\
    chmod -R 777 /ros2

COPY src/src/pkg_foo/requirements.txt /tmp/
RUN /ros2/venv/bin/python3 -m pip install -r /tmp/requirements.txt  &&\
    rm /tmp/requirements.txt

COPY docker/.bashrc /tmp

WORKDIR /ros2/ws