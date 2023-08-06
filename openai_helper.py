import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPEN_AI_KEY')

# inp = input('Write your message: \n')

def send_msg(msg):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages = [
            {
                'role': 'user',
                'content': msg
            }
        ],
        temperature=1,
        max_tokens=256,
    )
    # print(response)
    # print(response.choices[0]['message']['content'])
    return response.choices[0]['message']['content']


