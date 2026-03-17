#!/usr/bin/env python3
import sys
import rosbag
from cv_bridge import CvBridge
import cv2

bag_path = sys.argv[1] if len(sys.argv) > 1 else 'data/assignment_rosbag.bag'
topic = None
bridge = CvBridge()
count = 0

print("=== Extracting from rosbag ===")
for topic, msg, t in rosbag.Bag(bag_path).read_messages():
    if 'image' in topic.lower():
        cv_img = bridge.imgmsg_to_cv2(msg, "bgr8")
        if count == 0:
            cv2.imwrite("sample_first_frame.jpg", cv_img)
        count += 1

print(f"✅ Done! Total images: {count}")
print(f"Topic: {topic}")
print(f"Sample saved: sample_first_frame.jpg")
