Webcam Object Detection using YOLO and OpenCV
This project demonstrates real-time object detection using your webcam, the YOLO (You Only Look Once) algorithm, and OpenCV (cv2).

Features
Real-time object detection using a webcam
Utilizes YOLO for high-speed detection
Easy to set up and run
Requirements
Python 3.x
OpenCV
NumPy
YOLO weights and configuration files
Installation
Clone this repository:

sh
Copy code
git clone https://github.com/yourusername/webcam-object-detection.git
cd webcam-object-detection
Install the required packages:

sh
Copy code
pip install opencv-python numpy
Download YOLO weights and configuration files:

YOLOv3 weights: YOLOv3.weights
YOLOv3 config: yolov3.cfg
COCO names: coco.names
Place the downloaded files in the project directory.

Usage
Run the object detection script:

sh
Copy code
python detect.py
The script will start your webcam and display the video with detected objects highlighted.

License
This project is licensed under the MIT License.
