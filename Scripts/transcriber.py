import openai
import magic
import os

def transcribe_audio(audio_file, api_key):
    openai.api_key = api_key

    # Determine MIME type
    mime = magic.Magic(mime=True)
    mime_type = mime.from_buffer(audio_file.read(1024))
    audio_file.seek(0)  # Reset file pointer to the beginning

    # Correct MIME type for 'audio/x-wav'
    if mime_type == 'audio/x-wav':
        mime_type = 'audio/wav'

    print(f"Filename: {audio_file.filename}")
    print(f"MIME Type: {mime_type}")

    supported_formats = ['audio/flac', 'audio/x-m4a', 'audio/mpeg', 'audio/mp4', 'audio/mpeg', 'audio/mp3', 'audio/mpga', 'audio/ogg', 'audio/wav', 'audio/webm']

    if mime_type not in supported_formats:
        return f"Unrecognized file format. Supported formats: {supported_formats}"

    try:
        # Transcribe the audio
        audio_file.seek(0)  # Reset file pointer to the beginning
        response = openai.Audio.transcribe(
            model="whisper-1",
            file=audio_file,
            media_type=mime_type
        )
        transcription_text = response['text']
        return transcription_text
    except Exception as e:
        print(f"Error during transcription: {e}")
        return str(e)
