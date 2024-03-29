from openai import OpenAI

from config import Config
from promet import Promet

client = OpenAI(
    # This is the default and can be omitted
    api_key=Config.API_KEY,
    base_url=Config.BASE_URL,
)


def request_openai(input_text: str):
    return client.chat.completions.create(
        messages=[
            {"role": "system", "content": Promet},
            {"role": "user", "content": input_text}
        ],
        model=Config.MODEL
    ).choices[0].message.content
