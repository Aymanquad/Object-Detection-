from ultralytics import YOLO
import cv2
import cvzone
import math

#webcam-stuff
cap = cv2.VideoCapture(0)
cap.set(3, 1280) #setting width
cap.set(4, 720)  #setting height

# cap = cv2.VideoCapture("videos/people.mp4")


classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush", "pillow", "notebook", "pen", "pencil", "ruler",
              "eraser", "calculator", "desk", "lamp", "poster", "mirror", "shoes", "slippers", "blanket",
              "clothes", "hanger", "water bottle", "backpack", "headphones", "speakers", "calendar",
              "school bag", "glasses", "stapler", "tape", "glue", "folders", "binders", "markers",
              "highlighters", "whiteboard", "paintbrush", "paints", "art supplies", "laundry basket",
              "alarm clock", "printer", "paper", "textbook", "magazine", "tablet", "rug" , "ruler" , "pen" , "pencil" , "box",
              "charger" 
              ]


#creating the model
model = YOLO("../Yolo-Weights/yolov8l.pt")



while True:
    success , img = cap.read()
    results = model(img , stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1 , y1 , x2 , y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1) , int(y1) , int(x2) , int(y2)
            cv2.rectangle(img , (x1,y1) , (x2,y2) , (0, 255, 0) , 2)

            config = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])

            cvzone.putTextRect(img , f'{classNames[cls]} {config}' , (max(0, x1) , max(35,y1)), thickness=1 , scale=1)  #35 in y so that we can see the config even when the obj goes a bit out

    cv2.imshow("Image",img)  #used to show frames captured above
    cv2.waitKey(1)