import cv2
import numpy as np
import os
import urllib.request

def download_file(url, filename):
    if not os.path.isfile(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print("Download complete.")

download_dir = "C:/Users/karth/OneDrive/Documents/VS 1/Code Alpha/Task 4 - Object Detection and Tracking/"

yolo_weights_url = "https://pjreddie.com/media/files/yolov3.weights"
yolo_cfg_url = "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg"
coco_names_url = "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"

yolo_weights_path = os.path.join(download_dir, "yolov3.weights")
yolo_cfg_path = os.path.join(download_dir, "yolov3.cfg")
coco_names_path = os.path.join(download_dir, "coco.names")

download_file(yolo_weights_url, yolo_weights_path)
download_file(yolo_cfg_url, yolo_cfg_path)
download_file(coco_names_url, coco_names_path)

# Load YOLO
net = cv2.dnn.readNet(yolo_weights_path, yolo_cfg_path)
with open(coco_names_path, "r") as f:
    classes = f.read().strip().split('\n')

def calculate_centroid(bbox):
    x, y, w, h = bbox
    cx = x + (w // 2)
    cy = y + (h // 2)
    return (cx, cy)

# Open video capture
cap = cv2.VideoCapture(0)  

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape

    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    output_layers_names = net.getUnconnectedOutLayersNames()
    layer_outputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    # Process detections
    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  

                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = colors[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x, y + 20), font, 2, (255, 255, 255), 2)

    # Display the frame
    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
