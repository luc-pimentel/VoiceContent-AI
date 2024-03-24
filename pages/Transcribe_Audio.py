import streamlit as st
import os
from audio_recorder_streamlit import audio_recorder
from utils import get_final_transcript



st.title('Record Your Voice')


audio_bytes = audio_recorder(pause_threshold=10.0)
temp_audio_filename = "temp_audio.mp3"

if audio_bytes:
    st.audio(audio_bytes, format="audio/mp3")
        
        
button_isClicked = st.button("Get Transcription")


if button_isClicked:
    with st.spinner("Loading..."):
            
        with open(temp_audio_filename,"wb") as audio_file:
            audio_file.write(audio_bytes)
                
        transcript = get_final_transcript(temp_audio_filename)


        st.text_area('Transcript:', transcript, height=200)
        audio_file.close()
        os.remove(temp_audio_filename)