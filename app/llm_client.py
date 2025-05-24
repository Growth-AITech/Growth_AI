import os
from openai import OpenAI
from dotenv import load_dotenv
from prompt_builder import construir_prompt

load_dotenv()
api_key = os.getenv("togetherApiKey")

client = OpenAI(api_key=api_key, base_url="https://api.together.xyz/v1")

def generar_campania(data: dict) -> str:
    prompt = construir_prompt(data)
    response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800  # le damos más oxígeno
    )
    return response.choices[0].message.content
