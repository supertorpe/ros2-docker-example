# ros2-docker-example
ROS2 jazzy node example.

This project sets a ROS2 docker environment with a python venv, and supports vscode debugging, ruff and mypy validations.
It runs the container with the current user to prevent permission problems with hosts files.

build docker image
```
./scripts/exec.sh -c build
```

Run container in "shell" mode. Use this mode for development purposes. It allows you to attach VSCode to the container and build+run+debug the node.
```
./scripts/exec.sh -c shell
```

Run the node:
```
./scripts/exec.sh -c start
```

Stop the container:
```
./scripts/exec.sh -c stop
```
