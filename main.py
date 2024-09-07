import openai
import json
import time

keys = json.load(open('./keys.json'))
openai.api_key = keys['secret']

chat_completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{
        "role": "user",
        "content": "Listen to your"
    }]
)

chat_completion.to_dict()
