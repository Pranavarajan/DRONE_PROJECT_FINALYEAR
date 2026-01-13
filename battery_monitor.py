import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class BatteryMonitor(Node):
    def __init__(self):
        super().__init__('battery_monitor')
        self.battery = 100.0
        self.publisher_ = self.create_publisher(Float32, 'battery_level', 10)
        self.timer = self.create_timer(1.0, self.update_battery)
        self.get_logger().info('Battery Monitor Started')

    def update_battery(self):
        self.battery -= 1.0
        msg = Float32()
        msg.data = self.battery
        self.publisher_.publish(msg)
        self.get_logger().info(f'Battery level: {self.battery}%')

        if self.battery <= 20.0:
            self.get_logger().warn('LOW BATTERY!')


def main(args=None):
    rclpy.init(args=args)
    node = BatteryMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
