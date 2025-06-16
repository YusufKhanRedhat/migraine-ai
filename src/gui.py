# Placeholder for Streamlit GUI
import streamlit as st
from src.predict import predict_migraine

def main():
    st.title("Migraine Classifier")

    uploaded_file = st.file_uploader("Upload fMRI or CSV File", type=["nii", "nii.gz", "csv"])
    
    if uploaded_file is not None:
        result = predict_migraine(uploaded_file)
        st.success(f"Prediction: {result}")

