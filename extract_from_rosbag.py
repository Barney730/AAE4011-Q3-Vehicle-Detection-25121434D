#!/usr/bin/env python3
import rosbag
from cv_bridge import CvBridge
import cv2

bag_path = 'data/assignment_rosbag.bag'   # ← CHANGE TO YOUR BAG PATH
image_topic = None
bridge = CvBridge()
count = 0
width = height = 0

bag = rosbag.Bag(bag_path)
print("=== Rosbag Info ===")
print(bag.get_type_and_topic_info())

# Auto-detect first image topic
for topic, msg, t in bag.read_messages():
    if topic.endswith('/image_raw') or 'image' in topic.lower():
        image_topic = topic
        cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        height, width = cv_img.shape[:2]
        count += 1
        break

# Count all frames
for topic, msg, t in bag.read_messages(topics=[image_topic]):
    count += 1

bag.close()

print(f"\n✅ Extracted {count} frames")
print(f"Topic: {image_topic}")
print(f"Resolution: {width} x {height}")
