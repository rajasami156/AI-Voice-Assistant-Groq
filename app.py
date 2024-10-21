from flask import Flask, request, send_file, render_template
import tempfile
from text2speech import text2speech
from speech2text import speech2text
from flask_cors import CORS
from groq_service import execute



app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process-audio", methods=["POST"])
def process_audio_data():
    audio_data = request.files["audio"].read()

    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
        temp_audio.write(audio_data)
        temp_audio.flush()


    text = speech2text(temp_audio.name)
    if not text:
        return "Error: Could not transcribe audio.", 500  
    generated_answer = execute(f"Please respond to the users text: {text} in a friendly way")
    generated_speech = text2speech(generated_answer)
    if not generated_speech:
        return "Error: Could not generate speech.", 500  
    
    return send_file(generated_speech, mimetype='audio/mpeg')


@app.route("/check", methods=["GET"])
def check():
    return "Checking if this endpoint is working or not"



if __name__ == '__main__':
    app.run(debug=True, port = 8000)