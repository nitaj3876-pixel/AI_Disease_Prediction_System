import os
import joblib
import numpy as np

print("Current Folder :", os.getcwd())
print("NumPy Version :", np.__version__)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "models", "label_encoder.pkl")

print("Model :", MODEL_PATH)
print("Encoder :", ENCODER_PATH)

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

sample = np.zeros((1, 132))

prediction = model.predict(sample)

print(encoder.inverse_transform(prediction))