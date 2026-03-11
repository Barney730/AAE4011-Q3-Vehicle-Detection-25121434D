#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO
import time

class VehicleDetector:
    def __init__(self):
        rospy.init_node('vehicle_detector', anonymous=True)
        self.bridge = CvBridge()
        self.model = YOLO('yolov8n.pt')          # fast & accurate for vehicles
        self.pub = rospy.Publisher('/vehicle_detection/image', Image, queue_size=10)
        self.sub = rospy.Subscriber('/camera/image_raw', Image, self.callback)  # ← CHANGE TOPIC if needed
        self.fps = 0
        self.count = 0
        rospy.loginfo("✅ Vehicle detector ready (YOLOv8n)")

    def callback(self, msg):
        start = time.time()
        cv_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        
        results = self.model(cv_img, conf=0.5, verbose=False)
        annotated = results[0].plot()                     # draws boxes + labels + confidence
        
        # Count vehicles
        vehicle_count = sum(1 for r in results[0].boxes if int(r.cls) in [2,5,7])  # car, bus, truck
        
        # Stats overlay
        cv2.putText(annotated, f"Vehicles: {vehicle_count}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.putText(annotated, f"FPS: {self.fps:.1f}", (20, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        
        # Publish and show
        self.pub.publish(self.bridge.cv2_to_imgmsg(annotated, "bgr8"))
        cv2.imshow("Vehicle Detection (YOLOv8)", annotated)
        cv2.waitKey(1)
        
        self.fps = 1.0 / (time.time() - start)
        self.count += 1
        if self.count % 30 == 0:
            rospy.loginfo(f"Processed {self.count} frames | Vehicles: {vehicle_count}")

if __name__ == '__main__':
    try:
        VehicleDetector()
        rospy.spin()
    except rospy.ROSInterruptException:
        cv2.destroyAllWindows()
