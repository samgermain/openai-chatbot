from openai import OpenAI
import json
import time
from pprint import pprint

keys = json.load(open('./keys.json'))

client = OpenAI(api_key=keys['secret'])

completions = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "user", "content": "Listen to your"}
    ],
    max_tokens=1,  # number of words/punctuation
    n=5,  # number of choices
    temperature=2  # 0=standard and deterministic, 2=low probability responses
)

# completions_dict = completions.to_dict()
for i in range(len(completions.choices)):
    choices = completions.choices[i].message.content
    pprint(choices)
