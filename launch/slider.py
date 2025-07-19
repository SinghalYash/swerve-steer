from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    urdf_path = '/home/yash/steer_ws/src/swerve-steer/urdf/marsrover.urdf'
    
    with open(urdf_path, 'r') as file:
        urdf_content = file.read()

    return LaunchDescription([
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            parameters=[{'robot_description': urdf_content}]
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': urdf_content}]
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'base_link']
        )
    ])
