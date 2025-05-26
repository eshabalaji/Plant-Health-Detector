# 🌿 Plant Health Detector

## Overview
Crop diseases, especially in vital crops like **tomatoes** and **potatoes**, threaten agricultural productivity and food security. Early detection is crucial, but many farmers lack access to effective diagnostic tools. This project provides an **AI-powered solution** to detect and classify common diseases like **early blight** and **late blight**, helping minimize crop loss and pesticide overuse.

## 🎯 Objectives
- **Detect plant health**: Distinguish between healthy and diseased tomato and potato leaves.
- **Classify diseases**: Identify specific diseases such as *early blight* and *late blight*.
- **Provide insights**: Recommend treatments and preventive actions.
- **Improve accessibility**: Simple UI for web/mobile for uploading leaf images and receiving instant analysis.
- **Support sustainability**: Enable targeted treatments and reduce chemical misuse.

## 🧠 Tech Stack
- Python
- TensorFlow / Keras or PyTorch (for ML model)
- OpenCV (image processing)
- Streamlit / Flask / FastAPI (web interface)
- Dataset: PlantVillage

## 🚀 How It Works
1. **Upload** a leaf image (tomato or potato).
2. **Image processing** and prediction via trained ML model.
3. **Results** display the health status and disease name, with recommended actions.

---

## 🔍 Inference Code
Use `predict_plant_health.py` or the notebook version to:
- Load your trained `.h5` model from Google Drive
- Predict disease class from one or more leaf images
- View results directly in Colab with color-coded HTML output


## 📱 Usage
Clone the repository and run the app locally:
```bash
git clone https://github.com/your-username/plant-health-detector.git
cd plant-health-detector
pip install -r requirements.txt
python app.py
```

## 📦 Applications
1. *Smart farming and crop monitoring.*
2. *Educational and research tool in plant pathology.*
3. *Early warning system for agricultural extension workers.*

----
