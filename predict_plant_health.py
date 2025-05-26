from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os
from google.colab import drive
from IPython.display import Image, display, HTML

# 🔗 Mount Google Drive
drive.mount('/content/drive', force_remount=True)

# 📍 Load model from Google Drive
model_path = '/content/drive/MyDrive/Final_Updated_Plant_Disease_Model_latest.h5'
if not os.path.isfile(model_path):
    raise FileNotFoundError(f"Model file not found at: {model_path}")

model = load_model(model_path)

# 🔤 Class Labels (from model training)
class_names = [
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

# 🌿 Disease Names for Extraction
Diseases = [
    'Early_blight',
    'Late_blight',
    'Bacterial_spot',
    'Leaf_Mold',
    'Septoria_leaf_spot',
    'Spider_mites Two-spotted_spider_mite',
    'Target_Spot',
    'Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato_mosaic_virus',
    'healthy'
]

# 🔍 Model Input Shape
model_input_shape = model.input_shape[1:3]

# 📷 Prediction Function
def predict_image_class(image_paths):
    predictions_list = []

    for image_path in image_paths:
        img = load_img(image_path, target_size=model_input_shape)
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        predictions = model.predict(img_array)
        predictions_list.append(predictions)

    avg_predictions = np.mean(predictions_list, axis=0)
    predicted_class_index = np.argmax(avg_predictions)
    predicted_class_name = class_names[predicted_class_index]

    return predicted_class_name

# 🧠 Disease Extraction
def extract_disease(label):
    label = label.lower()
    found = [d for d in Diseases if d.lower() in label]
    return ' '.join(d.replace('_', ' ') for d in found)

# 🧪 Test Image Path(s)
test_image_paths = [
    '/content/2.JPG',
    '/content/2.JPG',
    '/content/2.JPG'
]

# 🎯 Perform Prediction
predicted_label = predict_image_class(test_image_paths)

# 🧾 Display Results
def finder():
    is_tomato = "tomato" in predicted_label.lower()
    crop_type = "Tomato" if is_tomato else "Potato"
    display(Image(test_image_paths[0]))
    display(HTML(f"<p style='color: green;'>{crop_type} Leaf Detected!!</p>"))

    result = extract_disease(predicted_label)
    if "healthy" in result.lower():
        display(HTML(f"<p style='color: green;'>{result}</p>"))
    else:
        display(HTML(f"<p style='color: red;'>{result}</p>"))

finder()
