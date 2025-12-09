import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from PIL import Image
import io

MODEL_PATH = "ml/models/wound_model.h5"

class WoundModel:
    def __init__(self):
        self.model = tf.keras.models.load_model(MODEL_PATH)
        self.labels = ["healthy", "mild_infection", "severe_infection"]

    def predict(self, img_bytes):
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        img = img.resize((224,224))
        arr = preprocess_input(np.array(img))
        arr = np.expand_dims(arr, axis=0)

        pred = self.model.predict(arr)[0]
        idx = int(np.argmax(pred))

        return {
            "label": self.labels[idx],
            "confidence": float(pred[idx]),
            "probabilities": {self.labels[i]: float(pred[i]) for i in range(3)}
        }

wound_model = WoundModel()
