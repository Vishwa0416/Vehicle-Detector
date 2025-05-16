# 🚗 Vehicle Detection App with YOLOv8 + Streamlit

This is an AI-powered image analysis tool built using **YOLOv8** and **Streamlit**. It allows users to upload an image and automatically detects various types of vehicles (car, bus, truck, motorcycle, etc.) within the image using a pre-trained object detection model.

## 🚀 Features

* 🧠 **Object Detection with YOLOv8**: Leverages a powerful model to detect and classify vehicles in real-time.
* 🖼️ **Image Upload Interface**: Easily upload images directly in the web UI.
* 📦 **Pre-trained Model**: Uses Ultralytics’ YOLOv8n model out of the box.
* 📋 **Instant Feedback**: Shows an annotated image and lists detected vehicles.
* 🧩 **Extensible Architecture**: Easy to upgrade with custom models or additional classes.

## 🧰 Technologies Used

* [Streamlit](https://streamlit.io/)
* [YOLOv8 via Ultralytics](https://github.com/ultralytics/ultralytics)
* [OpenCV](https://opencv.org/)
* [Python](https://www.python.org/)

## 📸 Demo

* Upload any image with vehicles and get real-time object detection with bounding boxes and labels.

## 🤝 Contributions

* Contributions, feedback, and feature requests are welcome! Feel free to fork the project, submit issues, or open pull requests.

## 📂 Getting Started

Clone the repository and run the Streamlit app locally:

```bash
git clone https://github.com/your-username/vehicle-detection-app
cd vehicle-detection-app
pip install -r requirements.txt
streamlit run vehicle_detector.py

