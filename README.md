# AAE4011-Q3-Vehicle-Detection-25121434D
# 1. Place rosbag
mkdir -p data
cp /path/to/your/assignment_rosbag.bag data/

# 2. Build
cd ~/catkin_ws   # or your workspace
catkin_make
source devel/setup.bash

# 3. Terminal 1 - Run detector
roslaunch vehicle_detection detector.launch

# 4. Terminal 2 - Play rosbag
rosbag play data/assignment_rosbag.bag --loop

# 5. You will see OpenCV window + green stats + rqt_image_view /vehicle_detection/image works
