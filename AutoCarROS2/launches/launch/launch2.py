import os
import subprocess

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable

def generate_launch_description():

    navpkg = 'autocar_nav'
    gzpkg = 'autocar_gazebo'
    descpkg = 'autocar_description'
    mappkg = 'autocar_map'

    world = os.path.join(get_package_share_directory(gzpkg), 'worlds', 'autocar.world')
    world = "/opt/ros/foxy/share/gazebo_plugins/worlds/gazebo_ros_ackermann_drive_demo.world"
    #urdf = os.path.join(get_package_share_directory(descpkg),'urdf', 'autocar.xacro')
    urdf = "/home/jason/.gazebo/models/prius_hybrid/model.urdf"
    rviz = os.path.join(get_package_share_directory(descpkg), 'rviz', 'view.rviz')
    
    navconfig = os.path.join(get_package_share_directory(navpkg), 'config', 'navigation_params.yaml')

    use_sim_time = LaunchConfiguration('use_sim_time', default='True')

    subprocess.run(['killall', 'gzserver'])
    subprocess.run(['killall', 'gzclient'])

    return LaunchDescription([
        # SetEnvironmentVariable(
        #     'RCUTILS_CONSOLE_OUTPUT_FORMAT', '[{severity}]: {message}'
        # ),

        # SetEnvironmentVariable(
        #     'RCUTILS_COLORIZED_OUTPUT', '1'
        # ),

        ExecuteProcess(
            cmd=['gazebo', world, 'libgazebo_ros_factory.so'],
        ),

        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'
        ),

        Node(
            package='robot_state_publisher',
            name='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=[urdf]
        ),
        
        # Node(
        #     package='rviz2',
        #     executable='rviz2',
        #     name='rviz2',
        #     arguments=['-d', rviz],
        #     output={'both': 'log'}
        # ),
        
        # Node(
        #     package = navpkg,
        #     name = 'localisation',
        #     executable = 'localisation.py',
        #     parameters = [navconfig]
        # ),
    ])

def main():

    generate_launch_description()

if __name__ == '__main__':
    main()
