# export_model_to_onnx.py
import nemo.collections.asr as nemo_asr
import os

# Ensure models directory exists
os.makedirs("models", exist_ok=True)

# Load the model
model = nemo_asr.models.EncDecCTCModel.restore_from("models/stt_hi_conformer_ctc_medium.nemo")

# Export to ONNX
model.export("models/stt_hi_conformer_ctc_medium.onnx")
print("✅ Export completed: models/stt_hi_conformer_ctc_medium.onnx")
