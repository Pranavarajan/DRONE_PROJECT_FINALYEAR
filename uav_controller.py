import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class UAVController(Node):
    def __init__(self):
        super().__init__('uav_controller')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.control_loop)
        self.angle = 0.0

    def control_loop(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.linear.y = 0.0
        msg.angular.z = 0.3
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = UAVController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
