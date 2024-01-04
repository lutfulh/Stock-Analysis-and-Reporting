import requests
import json
import os

def get_gpt3_response(prompt, temperature=0.7, max_tokens=150):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        return "No OpenAI API key found. Please set the OPENAI_API_KEY environment variable."

    messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}]

    url = 'https://api.openai.com/v1/chat/completions'
    headers = {'Content-Type': 'application/json', 'Authorization': f"Bearer {openai_api_key}"}
    data = {'model': "gpt-3.5-turbo", 'messages': messages, 'temperature': temperature, 'max_tokens': max_tokens}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=10)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code.
        completion = response.json()["choices"][0]["message"]["content"]
        return completion.strip()
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.Timeout:
        return "The request timed out."
    except Exception as e:
        return f"An error occurred: {e}"
