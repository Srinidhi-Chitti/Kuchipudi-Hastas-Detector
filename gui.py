import sys
import cv2
import json
import joblib
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QFileDialog, QWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

def classify_image(image_path, model_path="models/hasta_model.pkl"):
    clf, le = joblib.load(model_path)
    image = cv2.imread(image_path)
    image = cv2.resize(image, (128, 128)).flatten().reshape(1, -1)
    label_idx = clf.predict(image)[0]
    label = le.inverse_transform([label_idx])[0]
    return label

def load_meanings(json_path="hasta_meanings.json"):
    if not os.path.exists(json_path):
        return {}
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

class MudraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kuchipudi Mudra Analyzer")
        self.setGeometry(200, 200, 500, 400)

        self.image_label = QLabel("No image selected")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.result_label = QLabel("")
        self.meaning_label = QLabel("")
        self.select_button = QPushButton("Select Hand Image")
        self.select_button.clicked.connect(self.load_image)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.result_label)
        layout.addWidget(self.meaning_label)
        layout.addWidget(self.select_button)

        self.setLayout(layout)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            pixmap = QPixmap(file_path).scaled(200, 200, Qt.KeepAspectRatio)
            self.image_label.setPixmap(pixmap)
            self.show_prediction(file_path)

    def show_prediction(self, path):
        label = classify_image(path)
        meanings = load_meanings()
        meaning = meanings.get(label, "Meaning not found.")
        self.result_label.setText(f"Predicted Mudra: {lsabel}")
        self.meaning_label.setText(f"Meaning: {meaning}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MudraApp()
    window.show()
    sys.exit(app.exec_())
