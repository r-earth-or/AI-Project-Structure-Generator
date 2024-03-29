import openai

from config import Config
from promet import Promet

openai.api_base = Config.BASE_URL
openai.api_key = Config.API_KEY


def request_openai(input: str):
    return openai.Completion.create(
        engine=Config.MODEL,
        messages=[
            {"role": "system", "content": Promet},
            {"role": "user", "content": input}
        ]
    ).choices[0].text.strip()
