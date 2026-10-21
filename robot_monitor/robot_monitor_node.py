import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import Float32


class RobotMonitor(Node):

    def __init__(self):
        super().__init__('robot_monitor')

        self.battery_publisher = self.create_publisher(
            Float32, '/robot/battery_percentage', 10
        )

        self.temperature_publisher = self.create_publisher(
            Float32, '/robot/temperature_celsius', 10
        )

        self.battery = 25.0
        self.temperature = 48.0

        self.timer = self.create_timer(1.0, self.publish_status)

    def publish_status(self):
        self.battery = random.uniform(15.0, 100.0)
        self.temperature = random.uniform(25.0, 50.0)
        battery_msg = Float32()
        battery_msg.data = self.battery
        self.battery_publisher.publish(battery_msg)

        temperature_msg = Float32()
        temperature_msg.data = self.temperature
        self.temperature_publisher.publish(temperature_msg)

        self.get_logger().info(
            f'Battery: {self.battery:.1f}% | '
            f'Temperature: {self.temperature:.1f} C'
        )

        if self.battery < 30.0:
            self.get_logger().warning('LOW BATTERY!')

        if self.temperature > 40.0:
            self.get_logger().warning('HIGH TEMPERATURE!')

def main(args=None):
    rclpy.init(args=args)
    node = RobotMonitor()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
