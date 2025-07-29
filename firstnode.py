import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64MultiArray,Float64MultiArray

class FirstNode(Node):
    def __init__(self):
        super().__init__('KeyboardNode')

        self.velpub = self.create_publisher(Float64MultiArray,'/velocity_controller/commands',10)
        self.pospub = self.create_publisher(Int64MultiArray,'position_controller/commands',10)

    def main(self):

        while rclpy.ok():
            velocity = Float64MultiArray()
            velocity.data = [0.0,0.0,0.0,0.0]

            self.velpub.publish(velocity)

            print('msg sent')


if __name__ == '__main__':
    rclpy.init()
    node = FirstNode()
    node.main()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()




