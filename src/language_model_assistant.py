class LanguageModelAssistant:
    def __init__(self):
        # Initialize any necessary variables or objects
        self.transcribed_text = ""

    def record(self):
        # Record audio and save it to a file
        import pyaudio
        import wave

        chunk = 1024  # Record in chunks of 1024 samples
        sample_format = pyaudio.paInt16  # 16 bits per sample
        channels = 1
        fs = 44100  # Record at 44100 samples per second
        seconds = 3
        filename = "output.wav"

        p = pyaudio.PyAudio()  # Create an interface to PortAudio

        print('Recording')

        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)

        frames = []  # Initialize array to store frames

        # Store data in chunks for 3 seconds
        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Stop and close the stream 
        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        p.terminate()

        print('Finished recording')

        # Save the recorded data as a WAV file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()   

        self.voice_to_text()     
        
    def voice_to_text(self):
        # Transcribe the recorded audio 
        import os
        from google.cloud import speech_v1p1beta1 as speech
        from google.cloud.speech_v1p1beta1 import types

        # Set up Google Cloud authentication
        # Note that the environment variable GOOGLE_APPLICATION_CREDENTIALS must be set to the path of the JSON file that contains your service account key.
        # os.environ['GOOGLE_APPLICATION_CREDENTIALS']

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
            print('Prompt:', result.alternatives[0].transcript)

        # Send the request to Google Cloud Speech-to-Text API and get the response
        response = client.recognize(config=config, audio=audio)

        # Save the transcription to a text file
        with open('transcription.txt', 'w') as f:
            for result in response.results:
                f.write(result.alternatives[0].transcript + '\n')

        # Print a message to confirm that the transcription was saved
        print('Transcription saved to transcription.txt')            

    def text_to_chatgpt(self):   
        import openai
        import os

        # Set up your API token
        # note that the environment variable OPENAI_API_KEY must be set to your API key
        openai.api_key = os.getenv('OPENAI_API_KEY')

        # Open the text file containing the prompt
        with open('transcription.txt', 'r') as f:
            text = f.read()

        # Submit a prompt to ChatGPT
        model_engine = "gpt-3.5-turbo" 
        prompt = text
        response = openai.ChatCompletion.create(
            model=model_engine,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )        

        # Print the response
        print(response["choices"][0]["message"]["content"])    

        # Save the response to a text file
        with open('chatgpt_response.txt', 'w') as f:
            f.write(response["choices"][0]["message"]["content"])

        # Print a message to confirm that the response was saved
        print('Response saved to chatgpt_response.txt')

        self.text_to_audio()

    def text_to_audio(self):
        # Convert the response to audio
        import os
        from google.cloud import texttospeech_v1 as texttospeech
        from playsound import playsound

        # Set up Google Cloud authentication
        # Note that the environment variable GOOGLE_APPLICATION_CREDENTIALS must be set to the path of the JSON file that contains your service account key.
        # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] 

        # Initialize the Text-to-Speech client
        client = texttospeech.TextToSpeechClient()

        # Open the text file containing the response
        with open('chatgpt_response.txt', 'r') as f:
            text = f.read()


        # Set up the text input and audio configuration
        input_text = texttospeech.SynthesisInput(text=text)
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

