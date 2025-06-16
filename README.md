# Migraine Detection & Classification Software

## Overview
AI/ML-based tool for detecting and classifying migraine using tabular and fMRI data.

## Features
- Tabular & fMRI processing
- Random Forest & CNN models
- Streamlit GUI
- Docker support

## Quickstart
```bash
pip install -r requirements.txt
python main.py
```

## Docker
```bash
docker build -t migraine-ai .
docker run -p 8501:8501 migraine-ai
```
