import React, { useState, useEffect } from 'react';
import { Text, View, Button } from 'react-native';
import { Audio } from 'expo-av';
import * as Speech from 'expo-speech';

export default function SpeechToText() {
  const [recording, setRecording] = useState();
  const [transcript, setTranscript] = useState('');

  useEffect(() => {
    Audio.requestPermissionsAsync();
  }, []);

  const startRecording = async () => {
    const recording = new Audio.Recording();
    await recording.prepareToRecordAsync(Audio.RECORDING_OPTIONS_PRESET_HIGH_QUALITY);
    await recording.startAsync(); 
    setRecording(recording);
  }

  const stopRecording = async () => {
    await recording.stopAndUnloadAsync();

    const uri = recording.getURI(); 
    transcribeAudio(uri);
  }

  const transcribeAudio = async (uri) => {
    const transcript = await Speech.transcribeAsync({
      language: 'en-US',
      audio: uri
    });
    setTranscript(transcript);
  }

  return (
    <View>
      <Button title="Start Recording" onPress={startRecording} />
      <Button title="Stop Recording" onPress={stopRecording} />

      <Text>{transcript}</Text>
    </View>
  );
}