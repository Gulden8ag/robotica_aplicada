#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("py_test") # MODIFY NAME


def main(args=None):
    rclpy.init(args=args) 
    my_node = MyNode()  # MODIFY NAME
    rclpy.spin(my_node) 
    rclpy.shutdown()      

if __name__ == "__main__":
    main()