# drone_automation
Controller for drone automation using MAVROS

## Files  
- `controller.py`: Contains core controller class
- `waypoint.py`: Waypoint controller class for drone to traverse a list of points
- `utils.py`: A collection of utility functions for converversion, unwrapping etc,

## Requirements 
- [ROS](http://wiki.ros.org/ROS/Installation)
- [MAVROS](https://dev.px4.io/v1.9.0/en/ros/mavros_installation.html)
- PX4 [Firmware](https://github.com/PX4/Firmware.git)
- PX4 [Gazebo for MAVLink](https://github.com/PX4/sitl_gazebo)

## Usage 

For testing waypoint.py:

```python
$ roslaunch px4 mavros_posix_sitl.launch
$ python waypoint.py
```
***Note:*** *This should be done in seperate terminals* 

For testing iris_fpv_cam or iris_rplidar:
- Add both launch files to Firmware/launch directory
- Add the modified_warehouse.world file to Firmware/Tools/sitl_gazebo/worlds directory
- Add the tf_node.sh script to the Firmware directory

Now,you can simply do: 

```python
$ roslaunch px4 iris_fpv_cam.launch
```
or
```python
$ roslaunch px4 iris_rplidar.launch
```
Once both Gazebo and Rviz have been launched, you can run(in a new terminal):
```python
$ python waypoint.py
```
and check whether the feeds are being updated in Rviz


## TODO
- [X] Add waypoint controller
- [ ] Use `setpoint_velocity` with proportional control
- [ ] Incorporate obstacle detection using LIDAR / Camera

## Resources
- [GAAS](https://gaas.gitbook.io/guide/) (Generalized Autonomy Aviation System) Guide
- PX4 Development Guide [MAVROS Example](https://dev.px4.io/v1.9.0/en/ros/mavros_offboard.html)
