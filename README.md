# 🗣️ Hindi ASR FastAPI Service (ONNX)

This project provides a RESTful API to perform **automatic speech recognition (ASR)** for Hindi audio. It uses the `stt_hi_conformer_ctc_medium` model from NVIDIA NeMo, exported to ONNX format for optimized inference, and is served using **FastAPI**.

---

## 📦 Features

- 🎙️ Hindi ASR using NeMo Conformer CTC model
- ⚡ ONNX Runtime for fast inference
- 🚀 FastAPI backend with `/transcribe` endpoint
- ✅ WAV audio validation: mono, 16kHz, 5–10 sec

---

## 🛠️ Getting Started Without Docker

> For users running the service locally without Docker.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/hindi-asr-fastapi.git
cd hindi-asr-fastapi

### 2. Set Up Python Environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


### 3. Install Python Dependencies
pip install -r requirements.txt



## 4.Export the NeMo Model to ONNX
python export_model_to_onnx.py


## 5 Start the ASR Service
uvicorn app.main:app --reload
 

## 6  A simple Streamlit web interface is provided to interact with the ASR FastAPI service for quick testing and demos.
##Run the Streamlit app
Make sure your FastAPI server is running on http://localhost:8000, then start Streamlit:

streamlit run asr_ui.py

