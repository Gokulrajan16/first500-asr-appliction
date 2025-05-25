import torchaudio
import io

def load_wav(audio_bytes: bytes):
    waveform, sample_rate = torchaudio.load(io.BytesIO(audio_bytes))
    return waveform, sample_rate
