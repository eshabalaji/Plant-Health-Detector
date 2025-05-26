# predict_plant_health.py

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

# Model loading
model_path = '/content/drive/MyDrive/Final_Updated_Plant_Disease_Model_latest.h5'
if not os.path.isfile(model_path):
    raise FileNotFoundError(f"Model not found at: {model_path}")
model = load_model(model_path)

# Classes
class_names = [
    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight',
    'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

diseases = [
    'healthy', 'Bacterial_spot', 'Early_blight', 'Late_blight', 'Leaf_Mold',
    'Septoria_leaf_spot', 'Spider_mites Two-spotted_spider_mite',
    'Target_Spot', 'Tomato_Yellow_Leaf_Curl_Virus', 'Tomato_mosaic_virus'
]

# Image shape
input_shape = model.input_shape[1:3]

def predict_class(image):
    img = load_img(image, target_size=input_shape)
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    return class_names[np.argmax(predictions)]

def extract_disease(pred_class):
    pred_lower = pred_class.lower()
    found = [d for d in diseases if d.lower() in pred_lower]
    return ' '.join(d.replace('_', ' ') for d in found)
