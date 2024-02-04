import os
from google.cloud import texttospeech_v1 as texttospeech
from playsound import playsound

# Set up Google Cloud authentication
# Note that the environment variable GOOGLE_APPLICATION_CREDENTIALS must be set to the path of the JSON file that contains your service account key.
# os.environ['GOOGLE_APPLICATION_CREDENTIALS']

# Initialize the Text-to-Speech client
client = texttospeech.TextToSpeechClient()

# Set up the text input and audio configuration
input_text = texttospeech.SynthesisInput(text="The entire population on earth, of humans, land animals and sea creatures, all living things on the earth, was calculated for the first time in the year 1955 when it was thought that we had finally reached the approximate figure of 4.1 billion.")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Generate the audio
response = client.synthesize_speech(
    input=input_text, voice=voice, audio_config=audio_config
)

# Save the audio to a file
filename = "response.mp3"
with open(filename, "wb") as out:
    out.write(response.audio_content)

print("Audio content written to 'response.mp3'")

# Play the audio using playsound
playsound(filename)
