import launch
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import launch_ros.actions
import os
from launch_ros.actions import Node
import xacro
def generate_launch_description():
    pkg_path = launch_ros.substitutions.FindPackageShare('robotsim_package').find('robotsim_package')
    xacro_path = os.path.join(pkg_path, 'urdf', 'robotsim2.urdf.xacro')
    gazebo_launch_path = os.path.join(
        launch_ros.substitutions.FindPackageShare('gazebo_ros').find('gazebo_ros'),
        'launch', 'gazebo.launch.py'
    )

    robot_description = xacro.process_file(xacro_path).toxml()
    urdf_path = os.path.join(pkg_path, 'urdf', 'robotsim2.urdf')
    with open(urdf_path, 'w') as outfp:
        outfp.write(robot_description)
    print(robot_description)
    return launch.LaunchDescription([
        DeclareLaunchArgument('gui', default_value='true', description='Use joint_state_publisher_gui'),
        # Robot State Publisher
        launch_ros.actions.Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}]
        ),
        # Publishin joint states
        launch_ros.actions.Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}]
        ),
        IncludeLaunchDescription(PythonLaunchDescriptionSource(gazebo_launch_path)),
        # Gazebo import Model from Topic robot_description
        launch_ros.actions.Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'robotsim', '-topic', "/robot_description"],
            output='screen'
        )
        
    ])
generate_launch_description()