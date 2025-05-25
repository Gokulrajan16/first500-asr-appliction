import onnxruntime as ort
import numpy as np

class ONNXASRModel:
    def __init__(self, model_path: str):
        self.session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])

    def transcribe(self, audio_signal: np.ndarray, length: np.ndarray):
        ort_inputs = {
            self.session.get_inputs()[0].name: audio_signal,
            self.session.get_inputs()[1].name: length,
        }
        ort_outs = self.session.run(None, ort_inputs)
        # TODO: Add decoding logic here
        return "Decoded text (simulation)"
