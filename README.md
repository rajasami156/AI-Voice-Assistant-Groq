# 🎤 Voice-Activated AI Response System 🧠💬
This project is a Flask-based web application that enables users to record or upload an audio file. The application processes the audio by converting speech to text using Deepgram's API, generates a friendly AI response based on the transcribed text, and then converts the response back into speech. It integrates speech-to-text, AI text generation, and text-to-speech functionalities seamlessly.

### 🌟 Features
Speech-to-Text Conversion: Converts user-uploaded or recorded audio to text using Deepgram’s API.
AI Text Generation: Generates a friendly AI-based response to the transcribed text.
Text-to-Speech Conversion: Converts the AI-generated response back into speech and plays it for the user.
CORS Enabled: Supports Cross-Origin Resource Sharing (CORS) for accessing the API from different domains.

### 🚀 Getting Started
Prerequisites
Make sure you have the following tools installed:

Python 3.8+
pip (Python package manager)
A Deepgram API Key (which can be obtained by signing up on Deepgram’s platform)
Installation
Clone the repository and navigate into the project directory.

Set up a virtual environment (optional but recommended) to manage dependencies.

Install the required Python packages from the requirements.txt file.

Set up your environment variables in a .env file with your Deepgram API key to ensure the app connects with the API.

Running the Application
Run the Flask app to start the server.

Open a web browser and navigate to the local server URL provided in the terminal to access the application.

Once loaded, you can start recording or uploading audio, and the application will:

Transcribe the audio to text.
Generate a friendly AI response to the transcribed text.
Convert the response back to speech and allow you to listen to it.

### 📂 Project Structure
static/: Contains the static files (JavaScript and CSS) used for frontend interaction.
templates/: Includes the HTML files used for rendering the web pages.
app.py: The main Flask application file that handles the logic and API calls.
.env: Stores sensitive environment variables like the Deepgram API key.

### 🎨 User Experience
The interface is simple and intuitive, allowing users to easily record or upload audio.
The application provides real-time feedback with loaders and status messages.
After processing, the user can listen to the AI-generated response.

### 🛠️ Technologies Used
Flask: For the backend web framework.
Deepgram: For both speech-to-text and text-to-speech conversions.
JavaScript & HTML: For frontend interaction and recording audio.

### 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
