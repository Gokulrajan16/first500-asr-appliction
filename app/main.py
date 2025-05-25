from fastapi import FastAPI, UploadFile, File, HTTPException
from app.utils import load_wav
from app.model import ONNXASRModel
import numpy as np
import torch
import torchaudio

app = FastAPI()
asr_model = ONNXASRModel("models/stt_hi_conformer_ctc_medium.onnx")

def extract_features(waveform, sample_rate=16000, n_mels=80):
    if waveform.shape[0] > 1:
        waveform = torch.mean(waveform, dim=0, keepdim=True)
    mel_spectrogram = torchaudio.transforms.MelSpectrogram(
        sample_rate=sample_rate,
        n_fft=400,
        win_length=400,
        hop_length=160,
        n_mels=n_mels,
    )
    mel_feats = mel_spectrogram(waveform)
    log_mel_feats = torch.log(mel_feats + 1e-6)
    return log_mel_feats

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    if not file.filename.endswith(".wav"):
        raise HTTPException(status_code=400, detail="Only .wav files are supported.")
    
    audio_bytes = await file.read()
    waveform, sr = load_wav(audio_bytes)  # waveform shape: (channels, samples)
    
    if sr != 16000:
        raise HTTPException(status_code=400, detail="Audio must be sampled at 16kHz.")

    duration = waveform.shape[1] / sr
    if not 5 <= duration <= 10:
        raise HTTPException(status_code=400, detail="Audio must be 5–10 seconds long.")
    
    # Extract features expected by model (log-Mel spectrogram with 80 bins)
    features = extract_features(waveform, sample_rate=sr, n_mels=80)  # shape: (1, 80, time)
    
    # Add batch dimension (if not already)
    features = features.unsqueeze(0)  # shape: (1, 1, 80, time) or (batch, channel, feature_dim, seq_len)
    
    # ONNX model might expect shape: (batch, feature_dim, seq_len), so squeeze channel dim
    features = features.squeeze(1)  # shape: (1, 80, time)
    
    features_np = features.numpy().astype(np.float32)
    length = np.array([features_np.shape[2]], dtype=np.int64)

    transcription = asr_model.transcribe(features_np, length)
    return {"transcription": transcription}
