import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

st.title("🚗 Vehicle Detection App")
st.write("Upload an image, and I'll detect vehicles for you!")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    img_array = np.array(image)

    results = model.predict(img_array)

    result = results[0]

    vehicle_classes = ['car', 'truck', 'bus', 'motorcycle', 'bicycle']

    detected_vehicles = []
    annotated_img = result.plot()

    for box in result.boxes:
        cls = result.names[int(box.cls[0])]
        if cls in vehicle_classes:
            detected_vehicles.append(cls)

    st.image(annotated_img, caption="Detected Image", use_container_width=True)

    if detected_vehicles:
        st.success("Detected Vehicles:")
        for v in set(detected_vehicles):
            st.write(f"- {v}")
    else:
        st.warning("No vehicles detected.")
