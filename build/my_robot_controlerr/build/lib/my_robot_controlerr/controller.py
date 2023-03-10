#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class controller(Node):
    def __init__(self):
        super().__init__("vitesse_controller")
        self.cmd_vel_pub_= self.create_publisher(Twist, "/demo/cmd_vel",10)
        self.get_logger().info(" the node is start running")
        self.create_timer(0.5, self.send_vel)

    def send_vel(self):
        msg= Twist()
        msg.linear.x=1.0
        self.cmd_vel_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node= controller()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=='__main__':
    main()