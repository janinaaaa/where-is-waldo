from ultralytics import YOLO

model = YOLO('yolov10s.pt')
model.predict(
   source='https://media.roboflow.com/notebooks/examples/dog.jpeg',
   conf=0.25
)