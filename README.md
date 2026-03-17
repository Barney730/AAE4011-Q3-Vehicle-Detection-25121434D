# AAE4011 Assignment 1 — Q3: ROS-Based Vehicle Detection from Rosbag

> **Student Name:** Hung Yan Kin Barney | **Student ID:** 25121434D | **Date:** 17/3/2026

---

## 1. Overview

*This repository implements a complete ROS-based real-time vehicle detection pipeline using YOLOv8n on images from a rosbag recorded by a drone/UAV camera.*

## 2. Detection Method *(Q3.1 — 2 marks)*

*I chose YOLOv8n (Ultralytics) because it is single-stage, extremely fast (real-time on CPU), accurate for multiple vehicle classes (car, bus, truck, bicycle), and requires zero training. It automatically extracts features via CNN backbone — perfect for UAS edge deployment.*

## 3. Repository Structure
```bash
AAE4011-Q3-Vehicle-Detection-25121434D/
├── README.md
├── extract_from_rosbag.py
├── .gitignore
└── vehicle_detection/                  # ← ROS package
    ├── package.xml
    ├── CMakeLists.txt
    ├── launch/
    │   └── detector.launch
    └── scripts/
        └── vehicle_detector.py         # ← main detection node
```
## 4. Prerequisites

- Ubuntu 20.04 + ROS Noetic
- pip3 install ultralytics opencv-python
- sudo apt install ros-noetic-cv-bridge ros-noetic-image-view

## 5. How to Run *(Q3.1 — 2 marks)*
```bash
1. cd ~/catkin_ws
2. source devel/setup.bash
3. rosrun vehicle_detector bag_processor.py
```
## 6. Sample Results

![IMG_1784](https://github.com/user-attachments/assets/d432c6e4-28e8-4f19-ab9b-386ffe22e1aa)

![IMG_1785](https://github.com/user-attachments/assets/d5b32035-5aaf-47f7-a865-1008fa1b60e4)

![IMG_1786](https://github.com/user-attachments/assets/14f213f5-9e0d-4ca0-88a7-4638cef75439)

- Total frames: 1142,
- Vehicles detected: 2201

## 7. Video Demonstration *(Q3.2 — 5 marks)*

**Video Link:** YouTube (https://youtu.be/BARgCbP6Tvk?si=cKlspMAW03A1jENh)

## 8. Reflection & Critical Analysis *(Q3.3 — 8 marks, 300–500 words)*

### (a) What Did You Learn? *(2 marks)*

*I learned (1) how to read rosbag files offline with rosbag Python API and convert Image messages using CvBridge, and (2) how to integrate a modern deep-learning model (YOLOv8) into a ROS node with real-time publishing and visualization. These are core skills for any UAS perception pipeline.*

### (b) How Did You Use AI Tools? *(2 marks)*

*I used Grok (xAI) to generate the initial node structure and extraction script, then I manually debugged the topic name, added vehicle class filtering, FPS calculation, and OpenCV overlay myself. Benefit: saved hours of boilerplate coding. Limitation: the AI sometimes used wrong topic names or outdated ROS2 syntax, so I had to verify every line against official ROS docs. I also used ChatGPT to help write clean comments.*

### (c) How to Improve Accuracy? *(2 marks)*

- Fine-tune YOLOv8 on drone-specific aerial dataset (VisDrone or custom labeled PolyU images) — this would reduce false positives from birds/shadows because the model would learn top-down perspective.
- Add multi-sensor fusion (e.g., combine camera + LiDAR point cloud) — depth information would filter distant false detections and improve 3D bounding boxes.

### (d) Real-World Challenges *(2 marks)*

- Computational load on drone hardware: YOLOv8n is light but still needs GPU/Neural Processing Unit; a small drone may overheat or drop frames in real flight.
- Lighting and motion blur: rosbag is recorded in good conditions, but real UAS face changing sunlight, shadows, and fast camera motion — detection accuracy drops dramatically without domain adaptation or image enhancement.

## 9. References

- Ultralytics YOLOv8: https://docs.ultralytics.com
- ROS cv_bridge documentation
