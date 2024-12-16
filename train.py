from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Load Model
model = YOLO('yolov10s.pt')


model.train(
    data='dataset.yaml',  # Pfad zur YAML-Datei, die den Datensatz beschreibt
    epochs=100,  # Anzahl der Trainingsdurchläufe
    batch=-1,  # Batch-Größe
    name='custom_yolov10_model',  # Name des gespeicherten Modells
    pretrained=True  # Verwenden von vortrainierten Gewichten (Transfer Learning)
)