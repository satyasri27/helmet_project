🪖 Helmet Detection and Rider Monitoring System

A computer vision-based application that detects whether motorcycle riders are wearing helmets using a custom-trained YOLO model. The system processes images and identifies helmet violations in real time, helping improve road safety and traffic monitoring.

---

📌 Project Overview

Road accidents caused by riders not wearing helmets remain a major safety concern. This project leverages deep learning and computer vision techniques to automatically detect helmet usage from images or video feeds.

The model is trained using YOLO and can accurately identify riders wearing helmets and those violating safety regulations.

---

 ✨ Features

- Real-time helmet detection
- Custom-trained YOLO model
- Image-based detection through a simple interface
- Fast and accurate object detection
- Bounding box visualization
- Streamlit-based web application
- Easy deployment and scalability

---

🛠️ Technologies Used

- Python
- OpenCV
- YOLO (Ultralytics)
- NumPy
- Streamlit
- Deep Learning

---

📂 Project Structure

```text
helmet_project/
│
├── app.py                 # Streamlit application
├── enhancemulti.py        # Detection logic
├── final.pt               # Trained YOLO model
├── requirements.txt       # Dependencies
├── README.md
```

---

⚙️ Installation

1. Clone the Repository

```bash
git clone https://github.com/satyasri27/helmet_project.git
cd helmet_project
```

2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

🚀 Running the Application

Launch the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser.

---

🔍 How It Works

1. Upload an image through the Streamlit interface.
2. The YOLO model processes the image.
3. Riders and helmets are detected.
4. Detection results are displayed with bounding boxes.
5. Helmet violations can be identified instantly.

---

📊 Model Information

The project uses a custom-trained YOLO model (`final.pt`) for helmet detection.

Detected Classes

- Helmet
- No Helmet
- Rider

The model is optimized for fast inference and real-time performance.

---

🎯 Applications

- Traffic surveillance
- Smart city solutions
- Road safety monitoring
- Automated violation detection
- Computer vision research
- Educational projects

---

🔮 Future Improvements

- Number plate recognition
- Violation database management
- Multi-camera support
- Cloud deployment
- Mobile application integration
- Automated traffic violation reporting

---

👨‍💻 Author

**Naga Satya Sri Narina**

GitHub: https://github.com/satyasri27

---
📄 License

This project is developed for educational and research purposes. It may be modified and used for learning, experimentation, and academic projects.
