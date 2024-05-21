from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace

def generate_launch_description():
    vehicle_mirror_param_file = LaunchConfiguration('vehicle_mirror_param_file')
    container_name = LaunchConfiguration('container_name')
    use_distortion_corrector = LaunchConfiguration('use_distortion_corrector')
    
    DeclareLaunchArgument(name='vehicle_mirror_param_file', description='path to the file of vehicle mirror position yaml')
    DeclareLaunchArgument(name='container_name', default_value='buggy_node_container')
    
    top_lidar = GroupAction(
        actions=[
            PushRosNamespace(namespace='top'),
            IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('buggy_common_sensor_launch'), '/launch/buggy_node_container.launch.py']),
            launch_arguments=[#('topic', 'points_raw'), 
                            ('use_intra_process', 'True'),
                            ('use_multithread', 'False'),
                            ('vehicle_mirror_param_file', vehicle_mirror_param_file),
                            ('container_name', container_name),
                            ('use_distortion_corrector', use_distortion_corrector)])
        ]
    )
    
    right_lidar = GroupAction(
        actions=[
            PushRosNamespace(namespace='right'),
            IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('buggy_common_sensor_launch'), '/launch/buggy_node_container.launch.py']),
            launch_arguments=[#('topic', 'points_raw'), 
                            ('use_intra_process', 'True'),
                            ('use_multithread', 'False'),
                            ('vehicle_mirror_param_file', vehicle_mirror_param_file),
                            ('container_name', container_name),
                            ('use_distortion_corrector', use_distortion_corrector)])
        ]
    )

    left_lidar = GroupAction(
        actions=[
            PushRosNamespace(namespace='left'),
            IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('buggy_common_sensor_launch'), '/launch/buggy_node_container.launch.py']),
            launch_arguments=[#('topic', 'points_raw'), 
                            ('use_intra_process', 'True'),
                            ('use_multithread', 'False'),
                            ('vehicle_mirror_param_file', vehicle_mirror_param_file),
                            ('container_name', container_name),
                            ('use_distortion_corrector', use_distortion_corrector)])
        ]
    )

    bringup_with_namespace = GroupAction(
        actions=[
            PushRosNamespace(namespace='lidar'),
            top_lidar,
            left_lidar,
            right_lidar
        ]
    )

    return LaunchDescription([bringup_with_namespace])