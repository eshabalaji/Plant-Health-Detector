from google.colab import drive
drive.mount('/content/drive')

with open("app.py", "w") as f:
    f.write("""
import streamlit as st
from predict_plant_health import predict_class, extract_disease

# Streamlit layout
st.title("🌿 Plant Health Detector")
st.write("Upload at least 3 images of tomato or potato leaves for detection.")

uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    if len(uploaded_files) < 3:
        st.warning("Please upload at least 3 images.")
    else:
        tomato_detected = False
        potato_detected = False

        for file in uploaded_files:
            pred = predict_class(file)
            result = extract_disease(pred)

            if "tomato" in pred.lower():
                tomato_detected = True
                st.image("https://t4.ftcdn.net/jpg/03/27/96/23/360_F_327962332_6mb5jQLnTOjhYeXML7v45Hc5eED2GYOD.jpg")
                st.success("Tomato Detected!")
            elif "potato" in pred.lower():
                potato_detected = True
                st.image("https://t3.ftcdn.net/jpg/00/85/79/92/360_F_85799278_0BBGV9OAdQDTLnKwAPBCcg1J7QtiieJY.jpg")
                st.success("Potato Detected!")

            st.image(file, caption='Uploaded Image', use_container_width=True)
            if "healthy" in result:
                st.success(result)
            else:
                st.error(result)
""")
