#!/bin/python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ReceiverNode(Node):
    def __init__(self):
        super().__init__('receiver')
        self.message_topic = '/spgc/receiver'

        self.image_subscription = self.create_subscription(
            String,
            self.message_topic,
            self.print_message,
            10)


    def print_message(self, msg):
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)
    message_processor = ReceiverNode()
    rclpy.spin(message_processor)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
