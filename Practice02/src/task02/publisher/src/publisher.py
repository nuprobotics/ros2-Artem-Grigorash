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

        msg = String()
        msg.data = "Hello, ROS2!"
        self.message_publisher.publish(msg)

        self.timer = self.create_timer(1, lambda: self.message_publisher.publish(msg))

    def publish_message(self):
        msg = String()
        msg.data = "Hello, ROS2!"
        self.message_publisher.publish(msg)




def main(args=None):
    rclpy.init(args=args)
    message_processor = PublisherNode()
    rclpy.spin(message_processor)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
