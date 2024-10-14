import os
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    SpeakOptions,
)
load_dotenv()

def text2speech(text):
    try:
        SPEAK_OPTIONS = {"text": text}
        filename = "output.wav"

        deepgram = DeepgramClient(api_key=os.getenv("DG_API_KEY"))
        options = SpeakOptions(
            model="aura-asteria-en",
            encoding="linear16",
            container="wav"
        )

        response = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)

        if response:  
            return filename
        else:
            print("No response from Deepgram")
            return None

    except Exception as e:
        print(f"Exception: {e}")
        return None
