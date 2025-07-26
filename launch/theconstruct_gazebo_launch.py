import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument,IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_bot_gazebo = get_package_share_directory('swerve-steer')
    
    # description_package_name = 'my_robot_description'

    gazebo_models_path = os.path.join(pkg_bot_gazebo,'urdf')

    # if 'GAZEBO_MODEL_PATH' in os.environ:
    #     os.environ['GAZEBO_MODEL_PATH'] = os.environ['GAZEBO_MODEL_PATH'] + ':' +

