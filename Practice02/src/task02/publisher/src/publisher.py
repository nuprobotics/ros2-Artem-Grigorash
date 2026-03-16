#!/bin/python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher')
        self.message_topic = '/spgc/receiver'

        self.message_publisher = self.create_publisher(
            String,
            self.message_topic,
            10)

        self.declare_parameter('string', 'Hello, ROS2!')
        self.declare_parameter('rate_hz', 1.0)

        self.rate_hz = float(self.get_parameter('rate_hz').value)
        self.timer = self.create_timer(1.0 / self.rate_hz, self.publish_message)


        self.timer = self.create_timer(1, lambda: self.publish_message())

    def publish_message(self):
        text = self.get_parameter('string').value
        msg = String()
        msg.data = str(text)
        self.message_publisher.publish(msg)
        self.get_logger().info(msg.data + " published.")




def main(args=None):
    rclpy.init(args=args)
    message_processor = PublisherNode()
    rclpy.spin(message_processor)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
