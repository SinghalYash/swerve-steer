import rclpy
from rclpy.node import Node


class first(Node):
    def __init__(self): 
        super().__init__("firstnode")
    def firstfunction(self):
        print("hello world")



if __name__ == "__main__":
    rclpy.init()
    node = first()
    node.firstfunction()
    node.destroy_node()
    rclpy.shutdown()

