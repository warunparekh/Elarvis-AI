import os
import openai
import assistant.config as config

# Initialize OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY") or config.OPENAI_API_KEY

def chat(query):
    """
    Send the user query to OpenAI and return the response text.
    """
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}]
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"Chat error: {e}"