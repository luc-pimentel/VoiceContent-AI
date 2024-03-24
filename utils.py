import os
from typing import List
from decouple import config
from langchain.chains import LLMChain
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate




OPENAI_API_KEY = config("OPENAI_API_KEY")
WHISPER_PROMPT = config("WHISPER_PROMPT")
DRAFT_CORRECTOR_PROMPT = config("DRAFT_CORRECTOR_PROMPT")



class DraftCorrectorChainAnthropic:
    def __init__(self, model_name="claude-3-sonnet-20240229"):
        allowed_models = ["claude-3-sonnet-20240229", "claude-3-opus-20240229", "claude-3-haiku-20240307"]
        assert model_name in allowed_models, f"Invalid model name. Allowed models: {', '.join(allowed_models)}"

        ANTHROPIC_API_KEY = config("ANTHROPIC_API_KEY")
        
        self.chat_model = ChatAnthropic(model_name=model_name,
                                        anthropic_api_key=ANTHROPIC_API_KEY)
        
        system = DRAFT_CORRECTOR_PROMPT
        
        human = "{text}"
        
        self.prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
        
        self.chain = LLMChain(llm=self.chat_model, prompt=self.prompt)


    def run(self, text):
        response = self.chain.run({'text': text})
        return response


class Whisper:
    
    def __init__(self) -> None:
        from openai import OpenAI
        from decouple import config

        OPENAI_API_KEY = config("OPENAI_API_KEY")

        self.client = OpenAI(api_key = OPENAI_API_KEY)

    def get_transcript(self, audio_filepath, **kwargs):
        audio_file = open(audio_filepath, "rb")

        transcript = self.client.audio.transcriptions.create(
                        model="whisper-1", 
                        file=audio_file, 
                        response_format="text",
                        **kwargs)
        
        return transcript




def get_final_transcript(input_audio_file: str):
    import openai
    from moviepy.editor import AudioFileClip


    openai.api_key = OPENAI_API_KEY

    def _trim_audio(input_file, output_file, start_time, end_time):
        clip = AudioFileClip(input_file).subclip(start_time, end_time)
        clip.write_audiofile(output_file)


    """
    Returns the final transcription of the input audio file.

    Args:
        input_audio_file (str): The path to the input audio file.

    Returns:
        str: The final transcription of the input audio file.
    """

    audio_clip = AudioFileClip(input_audio_file)
    total_duration = audio_clip.duration



    chunk_size = 120

    # Initialize an empty list to store the transcriptions of each chunk
    transcripts: List[str] = []

    # Loop through the audio in 120-second intervals
    for start_time in range(0, int(total_duration), chunk_size):
        end_time = min(start_time + chunk_size, total_duration)

        # Trim the audio chunk using MoviePy or any other method you prefer
        chunk_output = f"chunk_{start_time}-{end_time}.mp3"
        _trim_audio(input_audio_file, chunk_output, start_time, end_time)

        # Transcribe the audio chunk
        chunk_audio_file = open(chunk_output, "rb")
        chunk_transcript = Whisper().get_transcript(chunk_output,
                                                    prompt = WHISPER_PROMPT)
        # Close the chunk audio file
        chunk_audio_file.close()

        # Delete the chunk audio file
        os.remove(chunk_output)

        
        transcripts.append(chunk_transcript)

    return " ".join(transcripts)