import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

st.set_page_config(page_title="Helmet Detection", layout="wide")

st.title("🪖 Helmet Detection System")

@st.cache_resource
def load_model():
    return YOLO("final.pt")

model = load_model()

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    img = np.array(image)

    if st.button("Detect Helmet"):
        results = model(img)

        annotated = results[0].plot()

        with col2:
            st.subheader("Detection Result")
            st.image(
                cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB),
                use_container_width=True
            )

        st.success("Detection completed!")
