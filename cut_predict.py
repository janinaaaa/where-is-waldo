from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import json
import analytics
from contextlib import redirect_stdout

OUTPUT_PATH = "output/cut/images"

analytics.write([], "cut/bounding_boxes")

# Load Model
model = YOLO('./best.pt')

# Colors and labels
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
labels = model.names


def predict_for_image(IMAGE_PATH, colors, labels):

    with open(os.devnull, 'w') as devnull:
        with redirect_stdout(devnull):
            results = model.predict(source=IMAGE_PATH, conf=0.25, verbose=False)
    
    # Load image
    img = cv2.imread(IMAGE_PATH)
    
    # Draw bounding boxes
    for result in results:
        for box in result.boxes:
            # Coordinates of the bounding box
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            data = {
                "image_path": IMAGE_PATH,
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2
            }

            analytics.append(data,"cut/bounding_boxes")
            # Confidence of the detected object
            conf = box.conf[0]
            
            # Label of the detected object
            class_id = int(box.cls[0])  # class_id is an integer
            label = labels[class_id]
            
            # Draw bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), colors[class_id % len(colors)], 2)
            
            # Text to be displayed
            text = f"{label}: {conf:.2f}"
            cv2.putText(img, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors[class_id % len(colors)], 2)
            
        
        # Save the image with bounding boxes
        output_image_path = IMAGE_PATH.replace('resized_images', 'output_images')
        os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
        cv2.imwrite(output_image_path, img)

done_count = 0
image_count = len(analytics.get("cut/images"))

for image_path in analytics.get("cut/images"):
    predict_for_image(image_path["path"], colors, labels)
    done_count += 1
    print(f"predict: {done_count}/{image_count}")