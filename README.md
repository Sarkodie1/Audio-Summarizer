Audio Summarizer API Documentation
Overview
The Audio Summarizer API allows users to upload audio files and receive a text summary of the audio content. This documentation outlines how to interact with the API, including endpoints, request/response formats, error handling, and usage examples.

Base URL
arduino
Copy code
http://audiosummariz-env.eba-nmjnb2ie.eu-north-1.elasticbeanstalk.com
API Endpoint
POST /summarize-call
This endpoint is used to upload an audio file for summarization.

Request
Method: POST
Content-Type: multipart/form-data
Request Parameters
file (required): The audio file to be summarized. Acceptable formats include .wav, .mp3, etc.
Example Request (using CURL)
bash
Copy code
curl -X POST "http://audiosummariz-env.eba-nmjnb2ie.eu-north-1.elasticbeanstalk.com/summarize-call" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@/path/to/your/audiofile.wav"
Request Body
Make sure to replace /path/to/your/audiofile.wav with the actual path to the audio file on your device.

Response
Content-Type: application/json
Successful Response
Status Code: 200 OK
Response Body:

json
Copy code
{
  "summary": "This is a summary of the audio content."
}
Error Responses
Status Code: 413 Request Entity Too Large
Description: The uploaded file exceeds the maximum allowed size (200MB).
Status Code: 405 Method Not Allowed
Description: The request method is not supported for this endpoint.
Status Code: 500 Internal Server Error
Description: An error occurred on the server while processing the request.
Error Handling
In case of an error, the API will return a JSON response with the following structure:

json
Copy code
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Error description."
  }
}
Example Error Response
json
Copy code
{
  "error": {
    "code": "413",
    "message": "Request Entity Too Large."
  }
}
Additional Information
File Size Limit: The maximum file size for uploads is 200MB.
Supported File Formats: .wav, .mp3, and other common audio formats.
Rate Limiting: Ensure that requests are made within the API usage limits to avoid throttling.
