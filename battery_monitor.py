import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class BatteryMonitor(Node):
    def __init__(self):
        super().__init__('battery_monitor')
        self.publisher = self.create_publisher(Float32, '/battery', 10)
        self.battery = 100.0
        self.timer = self.create_timer(1.0, self.update)

    def update(self):
        self.battery -= 1.5
        msg = Float32()
        msg.data = self.battery
        self.publisher.publish(msg)

        if self.battery <= 20:
            self.get_logger().warn("LOW BATTERY → RETURN TO BASE")

def main():
    rclpy.init()
    node = BatteryMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
