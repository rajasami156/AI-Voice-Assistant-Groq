import os
from dotenv import load_dotenv
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)

load_dotenv()


API_KEY = os.getenv("DG_API_KEY")


def speech2text(AUDIO_FILE):
    try:
        deepgram = DeepgramClient(API_KEY)

        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }
        
        options = PrerecordedOptions(
            model="nova-2",  # You can experiment with different models
            smart_format=True,
            language="en-US"  # Specify the language if applicable
        )

        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        print(f"Deepgram Response: {response}")  # Debugging print

        # Check if a valid transcript is returned
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
        if transcript:
            return transcript
        else:
            print("No transcript found in response.")
            return None

    except Exception as e:
        print(f"Exception in speech2text: {e}")
        return None



if __name__ == "__main__":
    print(speech2text("output.wav"))