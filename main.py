from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Load Model
model = YOLO('yolov10s.pt')

# Predict
results = model.predict(source='dog.jpeg', conf=0.25)

# Load image
img = cv2.imread('dog.jpeg')

# Colors and labels
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
labels = model.names

# Draw bounding boxes
for result in results:
    for box in result.boxes:
        # Coordinates of the bounding box
        x1, y1, x2, y2 = map(int, box.xyxy[0])

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

# Display the image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

# Train YOLO on custom dataset
# from ultralytics import YOLO
#
# model = YOLO('yolov10s.pt')
#
# # YOLO Training starten
# model.train(
#     data='path/to/dataset/data.yaml',  # Pfad zur YAML-Datei, die den Datensatz beschreibt
#     epochs=100,  # Anzahl der Trainingsdurchläufe
#     imgsz=640,  # Bildgröße
#     batch=16,  # Batch-Größe
#     name='custom_yolov10_model',  # Name des gespeicherten Modells
#     pretrained=True  # Verwenden von vortrainierten Gewichten (Transfer Learning)
# )

