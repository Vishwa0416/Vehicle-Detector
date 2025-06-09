# 🚗 Vehicle Detection App using YOLOv8 & Streamlit
An AI-powered computer vision web application that enables users to detect and classify vehicles in images with ease. Built with Ultralytics YOLOv8, Streamlit, and OpenCV, this app provides an intuitive interface for performing real-time vehicle detection.

# 🔍 Overview
This application allows users to upload an image, and with the help of YOLOv8 (You Only Look Once, version 8) — one of the most powerful object detection models — the app identifies and highlights various types of vehicles such as:

🚗 Cars

🚌 Buses

🚛 Trucks

🏍️ Motorcycles

🚲 Bicycles

The output includes an annotated image with bounding boxes and labels, as well as a detailed count and listing of detected vehicles.

# 🚀 Key Features
## 🧠 YOLOv8-Based Object Detection
Uses the YOLOv8n (nano) pre-trained model from Ultralytics.

High-speed inference and accurate results on a wide range of images.

## 🖼️ User-Friendly Image Upload Interface
Built with Streamlit, allowing users to upload any image with a simple drag-and-drop or file picker.

## 🎯 Annotated Output
Automatically generates and displays the image with bounding boxes around detected vehicles.

Labels each vehicle with its class (e.g., car, bus, truck).

## 📊 Detection Summary
Lists the types and counts of vehicles detected.

Helpful for quick analytics or reporting.

## ⚙️ Extensible and Modular Codebase
Easily switch to a custom-trained YOLOv8 model.

Add more classes or modify post-processing logic as needed.

# 🧰 Technologies Used
Technology	Purpose
Streamlit	For building the interactive web app
YOLOv8 (Ultralytics)	State-of-the-art object detection
OpenCV	Image processing and annotation
Python	Backend and application logic

# 📂 Getting Started
Follow the steps below to run the app locally:

bash
Copy
Edit
# Clone the repository
git clone https://github.com/your-username/vehicle-detection-app
cd vehicle-detection-app

# Install required dependencies
pip install -r requirements.txt

# Start the Streamlit app
streamlit run vehicle_detector.py
Ensure you have Python 3.8+ and the necessary permissions to use your GPU (optional but recommended for faster detection).

# 🤝 Contributions
We welcome all forms of contribution!
If you'd like to:

Add support for video/webcam input

Integrate a custom YOLOv8 model

Improve UI/UX

Report bugs or request features

Please feel free to open an issue or submit a pull request.

# 📌 Future Improvements
🎥 Real-time video stream detection

📸 Webcam integration for live capture

🧠 Custom-trained models for fine-grained vehicle categories

🌐 Deploy on the web (e.g., Streamlit Cloud or Hugging Face Spaces)

📝 License
This project is open-source and available under the MIT License.
