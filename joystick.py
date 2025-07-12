import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Bool

class JoystickNode(Node):
    def __init__(self):
        super().__init__('MyJoystickNode')
        self.joysub = self.create_subscription(Joy,"/joy",self.joy_callback,10)
        # self.test = self.create_publisher(Bool,"test",10)



    def joy_callback(self, msg):
        self.leftx = msg.axes[0]
        self.lefty = msg.axes[1]
        self.rightx = msg.axes[2]
        self.righty = msg.axes[3]
        self.lefttrigger = msg.axes[5]
        self.righttrigger = msg.axes[4]

        self.a = msg.buttons[0]
        self.b = msg.buttons[1]
        self.x = msg.buttons[3]
        self.y = msg.buttons[4]
        self.leftstick = msg.buttons[13]
        self.rightstick = msg.buttons[14]
        self.rb = msg.buttons[7]
        self.lb = msg.buttons[6]

        # self.get_logger().info(f"left stick x is {self.leftx}")
        # self.get_logger().info(f"left stick y is {self.lefty}")
        # self.get_logger().info(f"right stick x is {self.rightx}")
        # self.get_logger().info(f"right stick y is {self.righty}")
        # self.get_logger().info(f"left trigger is {self.lefttrigger}")
        # self.get_logger().info(f"right trigger is {self.righttrigger}")
        # print("hello world")

        self.get_logger().info(f"A Button state is {self.a}")
        self.get_logger().info(f"B Button state is {self.b}")
        self.get_logger().info(f"X Button state is {self.x}")
        self.get_logger().info(f"Y Button state is {self.y}")
        self.get_logger().info(f"Left stick state is {self.leftstick}")
        self.get_logger().info(f"Right stick state is {self.rightstick}")
        self.get_logger().info(f"LB state is {self.lb}")
        self.get_logger().info(f"RB state is {self.rb}")

    # def testcallback(self):
    #     self.mymsg = Bool()
    #     self.mymsg.data == True
    #     self.test.publish(self.mymsg)
    


def main():
    rclpy.init()
    node1 = JoystickNode()
    rclpy.spin(node1)
    node1.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

