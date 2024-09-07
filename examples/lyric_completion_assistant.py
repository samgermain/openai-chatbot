from openai import OpenAI
import json
import time
from pprint import pprint

keys = json.load(open('./keys.json'))
client = OpenAI(api_key=keys['secret'])

# initial prompt with system message and 2 task examples
messages = [
    {"role": "system", "content": "I am Roxette lyric completion assistant. When given a line from a song, I will provide the next line in the song."},
    {"role": "user", "content": "I know there's something in the wake of your smile"},
    {"role": "assistant", "content": "I get a notion from the look in your eyes, yeah"},
    {"role": "user", "content": "You've built a love but that love falls apart"},
    {"role": "assistant", "content": "Your little piece of Heaven turns too dark"},
    {"role": "user", "content": "Listen to your"},
]


# completions_dict = completions.to_dict()
for i in range(4):
    completions = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens=15,  # number of words/punctuation
        n=1,  # number of choices
        temperature=0,  # 0=standard and deterministic, 2=low probability responses
    )
    choice = completions.choices[0].message.content
    print(choice)
    new_message = {"role": "assistant", "content": choice}
    messages.append(new_message)
