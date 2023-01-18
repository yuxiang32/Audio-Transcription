# Install dependencies

# chco install ffmpeg

# Installing pytorch
# conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia

# Installing Whisper
# pip install git+https://github.com/openai/whisper.git -q

# pip install streamlit

import streamlit as st
import whisper
import ffmpeg

st.title("Audio Transcription")

# upload audio file with streaamlit
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])


model = whisper.load_model("base")
st.text("Model loaded")

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Done")
        st.markdown(transcription["text"])
    else:
        st.sidebar.error("Please upload an audio file")

st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)
