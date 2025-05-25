
# 📄 Project Description

## 🎯 Overview

This project provides a **Hindi Automatic Speech Recognition (ASR)** service built using [NVIDIA NeMo](https://developer.nvidia.com/nemo) and optimized with **ONNX Runtime** for efficient inference. The service is exposed via a lightweight and robust **FastAPI** server, allowing users to upload `.wav` audio files and receive transcriptions of spoken Hindi in real-time.

## 🧠 Key Features

* ⚡ **High-performance Inference**: Uses ONNX export of the `stt_hi_conformer_ctc_medium` model for optimized CPU execution.
* 🧪 **FastAPI Backend**: Clean, modern, and async-powered REST API for handling requests.
* 🔊 **Audio Validation**: Ensures uploaded files are 16kHz mono `.wav` files between 5 and 10 seconds in duration.
* 🐳 **Dockerized**: Easily containerized and deployable in any environment.

## 📦 What’s Inside

* `main.py`: FastAPI app exposing `/transcribe` endpoint.
* `model.py`: Wrapper class to load and run inference using ONNX model.
* `utils.py`: Utility to load and validate audio from binary input.
* `export_model_to_onnx.py`: Script to export NeMo model to ONNX format.
* `Dockerfile`: Production-ready containerization of the API.

## ✅ API Usage Example

Send a POST request with a `.wav` file (5–10 seconds, mono, 16kHz):

```bash
curl -X POST "http://localhost:8000/transcribe" \
  -H "accept: application/json" \
  -F "file=@sample.wav"
```

Expected response:


{
  "transcription": "आपका स्वागत है"
}


## 🚀 Run Instructions (Cloud/CI/CD Friendly)

If Docker is not installed locally, use:

* **GitHub Codespaces**
* **Replit**
* **Google Colab (with Docker runtime)**
* **Cloud IDEs like Gitpod**

Or run locally with Docker:


docker build -t hindi-asr .
docker run -p 8000:8000 hindi-asr


Before that, export the ONNX model once using:

python export_model_to_onnx.py



🖥️ Streamlit UI for Easy Interaction
Usage
1.Ensure the FastAPI backend is running at http://localhost:8000.
2.Run the Streamlit UI:

"streamlit run asr_ui.py"

3.Upload your .wav file (mono, 16kHz, 5–10 seconds) and click Transcribe to get the Hindi transcription displayed instantly.

This makes it easy to demo the ASR model without manually sending HTTP requests.
