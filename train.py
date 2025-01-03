from ultralytics import YOLO

# Load Model
model = YOLO('yolov10s.pt')

model.train(
    data='dataset.yaml',  # Dataset
    epochs=100,
    imgsz=256,  # Image Size
    batch=-1,  # Batch-Größe
    name='custom_yolov10_model',  # Name of trained model
    pretrained=True  # Pretrained Weights (Transfer Learning)
)