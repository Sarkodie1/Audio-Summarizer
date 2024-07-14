from flask import Flask, request, jsonify
from analyzer.transcriber import transcribe_audio
import os
from dotenv import load_dotenv
import openai

app = Flask(__name__)
load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return "Audio Analyzer API is running. Use /analyze endpoint to transcribe and summarize audio files."

@app.route('/analyze', methods=['POST'])
def analyze_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    audio_file = request.files['file']
    
    if not audio_file:
        return jsonify({'error': 'No file provided'}), 400

    try:
        transcription = transcribe_audio(audio_file, API_KEY)
        if "Unrecognized file format" in transcription:
            return jsonify({'error': transcription}), 400
        
        summary = analyze_transcription(transcription, API_KEY)
        return jsonify({
            'transcription': transcription,
            'summary': summary
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def analyze_transcription(transcription, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an audio analyzer AI. Analyze the audio and create a summary of the provided transcription. Respond in Markdown."},
            {"role": "user", "content": f"The audio transcription is: {transcription}"}
        ],
        temperature=0,
    )
    return response.choices[0].message['content']

if __name__ == '__main__':
    app.run(debug=True)
