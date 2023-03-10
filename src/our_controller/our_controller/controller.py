#!/usr/bin/env python3  
import  rclpy   
from rclpy.node import Node 
import time

class Mynode(Node): 
     import time
     def __init__(self):
        self.counter_=0
        super().__init__("first_node")
        self.create_timer(1.0, self.timerre)

     def timerre(self):
        self.get_logger().info("hello"+ str(self.counter_))
        self.counter_+=1
    


def main(args=None):
    rclpy.init(args=args)
    node= Mynode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=='__main__':
    main()
