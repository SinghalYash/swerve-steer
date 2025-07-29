import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import Joy
import numpy as np


class FirstNode(Node):
    def __init__(self):
        super().__init__('JoyNode')

        self.joysub = self.create_subscription(Joy,'/joy',self.joy_callback,10)
        self.velpub = self.create_publisher(Float64MultiArray,'/velocity_controller/commands',10)
        self.pospub = self.create_publisher(Float64MultiArray,'position_controller/commands',10)

    
    def joy_callback(self,msg):
        self.leftx = msg.axes[0]
        self.lefty = msg.axes[1]
        self.rightx = msg.axes[3]
        self.righty = msg.axes[4]
        self.lefttrigger = msg.axes[2]
        self.righttrigger = msg.axes[5]

        # self.get_logger().info(f"left stick x is {self.leftx}")
        # self.get_logger().info(f"left stick y is {self.lefty}")
        # self.get_logger().info(f"right stick x is {self.rightx}")
        # self.get_logger().info(f"right stick y is {self.righty}")
        # self.get_logger().info(f"left trigger is {self.lefttrigger}")
        # self.get_logger().info(f"right trigger is {self.righttrigger}")
    
    def main(self):
        rclpy.spin_once(self)
        rclpy.spin_once(self)     
        rclpy.spin_once(self)      
        rclpy.spin_once(self)


        while rclpy.ok():
            velocity = Float64MultiArray()
            turn = Float64MultiArray()

            scalevel = self.lefty * 10.0 
            print(np.sign(self.lefty))
            print(scalevel)
            velocity.data = [scalevel,scalevel,scalevel,scalevel]


            alpha = 0.0

            if self.lefty != 0:
                alpha = np.arctan(self.leftx/self.lefty)
                print(alpha)



            scaleturn = (self.righty * np.pi/2)
            # turn.data = [scaleturn,scaleturn,scaleturn,scaleturn]
            turn.data = [alpha,alpha,alpha,alpha]
            self.velpub.publish(velocity)

            self.get_logger().info("velocity msg sent")

            self.pospub.publish(turn)

            self.get_logger().info("turn msg sent")

            if self.righttrigger < 0.1:
                #right point turn
                speed = self.righttrigger *5
                velocity.data = [speed,-speed,speed,-speed]
                turn.data = [np.pi/4,-np.pi/4,-np.pi/4,np.pi/4]

                self.velpub.publish(velocity)
                self.pospub.publish(turn)

                self.get_logger().info("point turn right")

            if self.lefttrigger < 0.1:
                #left point turn
                speed = self.lefttrigger *5
                velocity.data = [-speed,speed,-speed,speed]
                turn.data = [np.pi/4,-np.pi/4,-np.pi/4,np.pi/4]

                self.velpub.publish(velocity)
                self.pospub.publish(turn)
                self.get_logger().info("point turn left")

            # if abs(self.leftx) > 0.5:
            #     #horizontal
            #     speed = self.leftx*5*np.sign(self.leftx)
            #     velocity.data = [speed,speed,speed,speed]
            #     actualturn = np.pi/2 *np.sign(self.leftx)
            #     turn.data = [actualturn,actualturn,actualturn,actualturn]

            #     self.velpub.publish(velocity)
            #     self.pospub.publish(turn)
            #     self.get_logger().info("travelling horizontally")
    



            rclpy.spin_once(self)


if __name__ == '__main__':
    rclpy.init()
    node = FirstNode()
    node.main()
    node.destroy_node()
    rclpy.shutdown()




