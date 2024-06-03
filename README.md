# Webcam Object Detection using YOLO and OpenCV

This project demonstrates real-time object detection using your webcam, the YOLO (You Only Look Once) algorithm, and OpenCV (cv2).

## Features

- Real-time object detection using a webcam
- Utilizes YOLO for high-speed detection
- Easy to set up and run

## Requirements

- Python 3.x
- OpenCV
- NumPy
- YOLO weights and configuration files

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/Aymanquad/Object-Detection-.git
    cd webcam-object-detection
    ```

2. Install the required packages:
    ```sh
    pip install opencv-python numpy
    ```

3. Download YOLO weights and configuration files:
    - YOLOv3 weights: [YOLOv3.weights](https://pjreddie.com/media/files/yolov3.weights)
    - YOLOv3 config: [yolov3.cfg](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
    - COCO names: [coco.names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

4. Place the downloaded files in the project directory.

## Usage

Run the object detection script:
```sh
python webcam.py
