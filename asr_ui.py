import streamlit as st
import requests

st.set_page_config(page_title="Hindi ASR", page_icon="🎙️")
st.title("🎙️ Hindi Speech-to-Text (ASR)")

# Upload audio file
uploaded_file = st.file_uploader("Upload a WAV file (16kHz, 5-10s)", type=["wav"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")

    if st.button("Transcribe"):
        with st.spinner("Transcribing..."):
            try:
                files = {'file': (uploaded_file.name, uploaded_file, "audio/wav")}
                response = requests.post("http://localhost:8000/transcribe", files=files)
                
                if response.status_code == 200:
                    transcription = response.json().get("transcription")
                    st.success("Transcription:")
                    st.write(f"📝 {transcription}")
                else:
                    st.error(f"❌ Error {response.status_code}: {response.json().get('detail')}")
            except Exception as e:
                st.error(f"🔌 Failed to connect to ASR backend: {e}")
