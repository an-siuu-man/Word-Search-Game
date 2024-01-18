from openai import OpenAI
import requests
from openai_api_key import key
grid_size = 14
num_of_words = 10
def get_words_for_grid(topic):
    topic_name = topic

    openai_api_key = key

    # OpenAI API endpoint
    api_endpoint = 'https://api.openai.com/v1/chat/completions'

    # Request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_api_key}'
    }

    # Request payload
    payload = {
        'model': 'gpt-4',
        'messages': [{'role': 'user', 'content': f'I am making a game of scrabble. Give me exactly {num_of_words} words (with no spaces in the words itself) in all capital letters in a comma separated list from the topic {topic_name} which are no longer than {grid_size-2} characters. 3 of them may be more uncommon than the rest.'}],
        'temperature': 0.8
    }

    # Make the API request
    response = requests.post(api_endpoint, json=payload, headers=headers)

    # Print the response
    k = response.json()['choices'][0]['message']['content'].split(', ')
    return k