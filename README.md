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
```python
$ roslaunch px4 mavros_posix_sitl.launch
$ python waypoint.py
```

***Note:*** *This should be done in seperate terminals* 


## TODO
- [X] Add waypoint controller
- [ ] Use `setpoint_velocity` with proportional control
- [ ] Incorporate obstacle detection using LIDAR / Camera

## Resources
- [GAAS](https://gaas.gitbook.io/guide/) (Generalized Autonomy Aviation System) Guide
- PX4 Development Guide [MAVROS Example](https://dev.px4.io/v1.9.0/en/ros/mavros_offboard.html)
