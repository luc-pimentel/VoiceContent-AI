import streamlit as st

st.title('Welcome to VoiceContent AI')

st.write("""
**VoiceContentAI** is the fastest way to create original content with AI. Here's how it works:

1. **Record Your Voice**: Start by recording your voice as you ramble on and express your ideas freely. Don't worry about coherence or structure at this stage – just let your thoughts flow naturally.

2. **Get a Rough Transcript**: Whisper AI model will transcribe your voice recording into a rough text transcript, capturing your initial ideas and concepts.

3. **Refine with AI**: Take the rough transcript and let Claude 3 work its magic. The AI will analyze the text, correct any errors, and restructure it into a coherent and well-organized format.

4. **Polished Content**: In just a few simple steps, you'll have a polished piece of content that's ready to be published or shared. VoiceContentAI takes the hassle out of content creation by allowing you to express your ideas naturally through voice, while leveraging the power of AI to refine and polish the final output.

## Customizing Prompts and API Keys

VoiceContentAI allows you to customize the prompts used by the AI and the API keys for various services.
Simply change the variables in the .env file.         
""")



#python -m streamlit run auth_page.py