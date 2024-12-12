#!/usr/bin/env python3

"""Example Node."""

from __future__ import annotations

import os

import rclpy
from rclpy.node import Node

ros2_threads = int(os.environ.get("ROS2_THREADS", "2"))


class BarNode(Node):
    """Example Node."""

    def __init__(self) -> None:
        """Initialize the node."""
        super().__init__("bar_node")  # Node name

        self.logger = self.get_logger()

        self.logger.info("Node started")


def main(args: list[str] | None = None) -> None :
    """Start the node."""
    rclpy.init(args=args)
    node = BarNode()
    executor = rclpy.executors.MultiThreadedExecutor(num_threads=ros2_threads)
    rclpy.spin(node, executor)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
