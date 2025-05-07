# ROS2 Differential Robot Simulation
## Launch Simulation :
```
source ~/ros2_ws/install/setup.sh
colcon build
ros2 launch robotsim_package simulation.launch.py
```
![image](https://github.com/user-attachments/assets/ab20a6bf-5d5f-4384-be70-695fc5e38614)

## Control :
By cmd_vel topic : 
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
## Mapping and Navigation :
```
ros2 launch slam_toolbox online_async_launch.py
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=True
```
## saving Map :
```
ros2 run nav2_map_server map_saver_cli -f map1 #save in folder pgm as map1.pgm (in the directory of the instruction or ~/..) 
```
![map1](https://github.com/user-attachments/assets/59c593bc-0437-4e28-8e56-29a791d91dda)
