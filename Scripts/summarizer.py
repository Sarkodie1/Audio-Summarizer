import openai

MODEL = 'gpt-3.5-turbo-0125'

def summarize_text(transcription_text, api_key):
    """
    Summarize the transcribed text using OpenAI's GPT-3.5-turbo model.

    Parameters:
    - transcription_text: The text to summarize
    - api_key: OpenAI API key

    Returns:
    - summary text
    """
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": """You are an audio analyzer AI. 
            Analyze the audio and create a summary of the provided transcription. Respond in Markdown."""},
            {"role": "user", "content": f"The audio transcription is: {transcription_text}"}
        ],
        temperature=0,
    )
    return response['choices'][0]['message']['content']
