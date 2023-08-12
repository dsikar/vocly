# Set up Google Cloud authentication
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/daniel/.ssh/vocly-395719-166a8748da49.json'

import os
from google.cloud import speech_v1p1beta1 as speech
from google.cloud.speech_v1p1beta1 import types

# Set up Google Cloud authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/daniel/.ssh/vocly-395719-166a8748da49.json'

# Initialize the Speech client
client = speech.SpeechClient()

# File name
filename = "output.wav"

# Read the audio file
with open(filename, 'rb') as audio_file:
    content = audio_file.read()

# Set up the audio type and configuration
audio = types.RecognitionAudio(content=content)
config = types.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    # Ensure you set the sample rate hertz according to your recording. Here, 44100 is assumed.
    sample_rate_hertz=44100,
    language_code="en-US",
)

# Send the request to Google Cloud Speech-to-Text API and get the response
response = client.recognize(config=config, audio=audio)

# Print the transcription
for result in response.results:
    print('Transcript:', result.alternatives[0].transcript)

