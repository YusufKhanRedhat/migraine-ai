# Placeholder for Streamlit GUI
import streamlit as st

st.set_page_config(page_title="Migraine Detection", layout="centered")

st.title("🧠 Migraine Detection AI")
st.write("Upload an fMRI or CSV file to detect and classify migraine type.")

uploaded_file = st.file_uploader("Choose a file", type=["nii", "nii.gz", "csv"])

if uploaded_file is not None:
    st.success(f"File uploaded: {uploaded_file.name}")
    # Add prediction logic here
else:
    st.info("Please upload a valid fMRI (.nii/.nii.gz) or CSV file.")
