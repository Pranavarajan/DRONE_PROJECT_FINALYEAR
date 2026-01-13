from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose'],
            output='screen'
        ),

        Node(
            package='uav_core',
            executable='uav_controller',
            output='screen'
        ),

        Node(
            package='uav_core',
            executable='battery_monitor',
            output='screen'
        ),
    ])
