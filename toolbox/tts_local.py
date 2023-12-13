from TTS.api import TTS

# Running a multi-speaker and multi-lingual model
#tts_api = TTS() # <-- Add this line
# List available 🐸TTS models and choose the first one
#model_name = tts_api.list_models()[0]
# Init TTS

# For models, do "tts --list_models" to see available models
tts = None

def set_tts(model:str):
    global tts
    tts = TTS(model_name=model, progress_bar=False).to("cpu")

async def tts_wav(client, text:str, output_path:str, spkr=0, spd=1.0):
    """
    Params
    ------
    text: str
        Text to be converted to speech

    Returns
    -------
    None
    """

    language = tts.languages
    if language is not None:
        language = language[0]

    speaker = tts.speakers
    if speaker is not None:
        print("speaker changed")
        speaker = speaker[spkr]

    def blocking_func():
        tts.tts_to_file(text, file_path=output_path, speaker=speaker, langauge=language, speed=spd)

    await client.loop.run_in_executor(None, blocking_func)

