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
Below is an example of how to integrate the API into a React Native app using the `axios` library.

Step 1: Install Axios
First, install axios if you haven't already:
```bash
npm install axios
```
Step 2: Create a Function to Upload and Summarize Audio
```javascript
import axios from 'axios';

const BASE_URL = 'http://audiosummariz-env.eba-nmjnb2ie.eu-north-1.elasticbeanstalk.com';

const summarizeAudio = async (fileUri) => {
  const formData = new FormData();
  formData.append('file', {
    uri: fileUri,
    type: 'audio/wav',
    name: 'audio.wav'
  });

  try {
    const response = await axios.post(`${BASE_URL}/summarize-call`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });

    return response.data.summary;
  } catch (error) {
    console.error('Error uploading file:', error.response ? error.response.data : error.message);
    throw error;
  }
};

export default summarizeAudio;
```
Step 3: Use the Function in Your Component
```javascript
import React, { useState } from 'react';
import { View, Button, Text } from 'react-native';
import * as DocumentPicker from 'expo-document-picker';
import summarizeAudio from './path/to/your/summarizeAudioFunction';

const AudioSummarizer = () => {
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);

  const pickDocument = async () => {
    const result = await DocumentPicker.getDocumentAsync({
      type: 'audio/*'
    });

    if (result.type === 'success') {
      setLoading(true);
      try {
        const summaryText = await summarizeAudio(result.uri);
        setSummary(summaryText);
      } catch (error) {
        console.error('Error summarizing audio:', error);
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <View>
      <Button title="Pick an Audio File" onPress={pickDocument} />
      {loading ? <Text>Loading...</Text> : <Text>{summary}</Text>}
    </View>
  );
};

export default AudioSummarizer;
```
## Error Handling
### Common Errors
413 Request Entity Too Large: Ensure the uploaded file is within the allowed size limit.

400 Bad Request: Check the file format and the request structure.
## Debugging Tips
Verify the API endpoint URL.
Ensure the headers and form data are correctly set.
Check the server logs for detailed error messages.
