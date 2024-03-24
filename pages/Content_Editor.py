import streamlit as st
from utils import DraftCorrectorChainAnthropic



st.title('Edit Your Transcript Into A Post')


draft_paragraph = st.text_input('Please insert your transcript:')



chunk_size = st.number_input('Chunk Size', min_value = 10,value = 1500, step = 1)

button_isClicked = st.button("Edit Your Trascript")


if button_isClicked:
    with st.spinner("Loading..."):

        response_text = ""

        for i in range(0, len(draft_paragraph), chunk_size):
            chunk = draft_paragraph[i:i+chunk_size]
            response_chunk = DraftCorrectorChainAnthropic().run(chunk)
            
            response_text += response_chunk

        st.text_area('Formatted Transcript:', response_text,height = 200)
        button_isClicked = False
        

