from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    urdf_path = '/home/yash/steer_ws/src/swerve-steer/urdf/marsrover.urdf'
    
    # Read URDF file
    with open(urdf_path, 'r') as file:
        robot_description = file.read()

    gazebo_launch_path = os.path.join(get_package_share_directory('gazebo_ros'),'launch','gazebo.launch.py')

    return LaunchDescription([
        # 1. Launch Gazebo (empty world)
        IncludeLaunchDescription(PythonLaunchDescriptionSource([gazebo_launch_path])),

        # 2. Publish robot description to parameter server
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        # 3. Spawn robot into Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'mars_rover',
                '-topic', 'robot_description',
                '-x', '0',
                '-y', '0',
                '-z', '5.0',
                '--ros-args'
            ],
            output='screen'
        )
    ])
