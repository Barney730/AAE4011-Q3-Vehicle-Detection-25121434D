cmake_minimum_required(VERSION 3.0.2)
project(vehicle_detection)
find_package(catkin REQUIRED COMPONENTS rospy cv_bridge sensor_msgs)
catkin_package()
catkin_install_python(PROGRAMS scripts/vehicle_detector.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
