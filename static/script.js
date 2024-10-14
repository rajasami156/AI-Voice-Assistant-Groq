let mediaRecorder;
let recordedChunks = [];

// Start recording
document.getElementById('start-recording').addEventListener('click', function() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            mediaRecorder.ondataavailable = function(event) {
                if (event.data.size > 0) {
                    recordedChunks.push(event.data);
                }
            };

            mediaRecorder.onstop = function() {
                const blob = new Blob(recordedChunks, { type: 'audio/wav' });
                recordedChunks = [];

                // Send the recorded audio blob to the Flask backend
                processAudio(blob);
            };

            // Update button states
            document.getElementById('start-recording').disabled = true;
            document.getElementById('stop-recording').disabled = false;
        })
        .catch(error => {
            console.error('Error accessing audio stream:', error);
        });
});

// Stop recording
document.getElementById('stop-recording').addEventListener('click', function() {
    mediaRecorder.stop();
    document.getElementById('start-recording').disabled = false;
    document.getElementById('stop-recording').disabled = true;
});

// Send recorded audio for processing
function processAudio(audioBlob) {
    const loader = document.getElementById('loader');
    const errorMessage = document.getElementById('error-message');
    const output = document.getElementById('output');
    const audioPlayer = document.querySelector('.audio-player');

    const formData = new FormData();
    formData.append('audio', audioBlob, 'recording.wav');

    loader.style.display = 'block'; // Show loader
    errorMessage.style.display = 'none'; // Hide any previous errors
    output.style.display = 'none'; // Hide transcript until processed
    audioPlayer.style.display = 'none'; // Hide audio player

    fetch('/process-audio', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to process audio');
        }
        return response.blob();
    })
    .then(blob => {
        const audioUrl = URL.createObjectURL(blob);
        document.getElementById('generated-audio').src = audioUrl;
        loader.style.display = 'none'; // Hide loader
        audioPlayer.style.display = 'block'; // Show audio player
    })
    .catch(error => {
        loader.style.display = 'none'; // Hide loader
        errorMessage.textContent = error.message;
        errorMessage.style.display = 'block'; // Show error message
        console.error('Error:', error);
    });
}
