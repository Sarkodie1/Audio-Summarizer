# Audio Summarizer API Documentation

## Overview
This document provides comprehensive instructions for integrating the Audio Summarizer API with a React Native app. The API allows users to upload an audio file and receive a summarized text version of the audio content.

## Base URL
http://audiosummariz-env.eba-nmjnb2ie.eu-north-1.elasticbeanstalk.com


## Endpoints

### 1. `/summarize-call`
- **Method**: `POST`
- **Description**: Upload an audio file to get a summarized text response.

#### Request
- **URL**:
## POST /summarize-call

- **Headers**:
```json
{
  "Content-Type": "multipart/form-data"
}
```
**Form Data:**
`file`: The audio file to be summarized. (e.g., file=@path/to/your-file.wav)

**Response**
Success (HTTP 200):
```json
{
  "summary": "This is the summarized text of the audio file."
}
```
Error (HTTP 400/500):
{
  "detail": "Error message describing what went wrong."
}


## Example Usage
**cURL**
```bash
curl -X POST "http://audiosummariz-env.eba-nmjnb2ie.eu-north-1.elasticbeanstalk.com/summarize-call" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@/path/to/your-file.wav"
```

## React Native Integration
**Prerequisites**
Ensure you have the following libraries installed in your React Native project:

`react-native-callkeep`
`react-native-audio-record`
`react-native-fs`
### Step-by-Step Guide**
**1. Setup CallKeep and AudioRecord**
Install and configure the necessary libraries to handle call events and record audio.

```bash
npm install react-native-callkeep react-native-audio-record react-native-fs
```

**2. Capture Call Audio**
Use the following code to handle call events and record audio:
```javascript
import { useEffect } from 'react';
import CallKeep from 'react-native-callkeep';
import AudioRecord from 'react-native-audio-record';
import RNFS from 'react-native-fs';

const options = {
  sampleRate: 16000,  // 16kHz
  channels: 1,        // mono
  bitsPerSample: 16,  // 16-bit
  wavFile: 'call_audio.wav'  // output file name
};

AudioRecord.init(options);

const startRecording = () => {
  AudioRecord.start();
};

const stopRecording = async () => {
  const audioFile = await AudioRecord.stop();
  return audioFile;
};

useEffect(() => {
  CallKeep.addEventListener('answerCall', () => {
    startRecording();
  });

  CallKeep.addEventListener('endCall', async () => {
    const audioFile = await stopRecording();
    uploadAudioFile(audioFile);
  });

  return () => {
    CallKeep.removeEventListener('answerCall');
    CallKeep.removeEventListener('endCall');
  };
}, []);
```

**3. Upload Audio File and Get Summary**
Use the following code to upload the recorded audio file to the API and get the summarized text:
```javascript
const uploadAudioFile = async (filePath) => {
  const file = {
    uri: `file://${filePath}`,
    type: 'audio/wav',
    name: 'call_audio.wav'
  };

  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await fetch('http://audiosummariz-env.eba-nmjnb2ie.eu-north-1.elasticbeanstalk.com/summarize-call', {
      method: 'POST',
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      body: formData
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const result = await response.json();
    console.log('Summary:', result.summary);
    alert(`Summary: ${result.summary}`);
  } catch (error) {
    console.error('Error uploading file:', error);
    alert('Failed to upload and summarize audio.');
  }
};
```

## Detailed Flow
**Recording Call Audio:**

Start Recording: The `startRecording` function initiates audio recording when the call is answered.
Stop Recording: The `stopRecording` function stops recording when the call ends and returns the path to the recorded audio file.

**Uploading Audio File:**

Prepare File: The recorded audio file is prepared for upload as a `multipart/form-data` request.
API Request: The audio file is uploaded to the API endpoint `/summarize-call`.

**Receiving Summarized Text:**

API Response: The API processes the audio file and returns a JSON object containing the summarized text.
Display Summary: The summarized text is displayed in the app.

   
## Error Handling
### Common Errors
413 Request Entity Too Large: Ensure the uploaded file is within the allowed size limit.

400 Bad Request: Check the file format and the request structure.
## Debugging Tips
Verify the API endpoint URL.
Ensure the headers and form data are correctly set.
Check the server logs for detailed error messages.
