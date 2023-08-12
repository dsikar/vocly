import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import SpeechToText from './SpeechToText';

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Speech to Text</Text>
      <SpeechToText />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
