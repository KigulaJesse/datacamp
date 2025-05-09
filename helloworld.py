# import os
# from dotenv import load_dotenv, dotenv_values
from openai import OpenAI
# load_dotenv()
# KEY = os.getenv("API-KEY")
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn."
        }
    ]
)

print(completion.choices[0].message.content)