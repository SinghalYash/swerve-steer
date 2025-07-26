from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    urdf_path = '/home/yash/steer_ws/src/swerve-steer/urdf/marsrover.urdf'
    world_path = '/home/yash/steer_ws/src/swerve-steer/worlds/empty_with_ground.world'
    ros2_controllers_path = '/home/yash/steer_ws/src/swerve-steer/config/joint_controller.yaml'

    # Read URDF file
    with open(urdf_path, 'r') as file:
        robot_description = file.read()

    gazebo_launch_path = os.path.join(get_package_share_directory('gazebo_ros'),'launch','gazebo.launch.py')

    return LaunchDescription([
        # 1. Launch Gazebo (empty world)
        IncludeLaunchDescription(PythonLaunchDescriptionSource([gazebo_launch_path]),
                                 launch_arguments={'world':world_path,'verbose':'true'}.items()
                                 ),

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
                '-z', '7.0',
                '--ros-args'
            ],  
            output='screen'
        ),

        Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[ros2_controllers_path],
        ),

        #load_joint_state_controller
        ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active',
             'joint_state_broadcaster'],
        output='screen'
        ),

        #load whichever controller
        ExecuteProcess(
            cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'velocity_controller'],
            output='screen'),

    



        
    ])
