import openai
import os
from dotenv import load_dotenv
import time

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_chatgpt(question: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message['content']

# Pergunta a ser feita
question = "A Zapflow vai abrir escritório em Moscow?"
answer = ask_chatgpt(question)

print(f"Resposta do ChatGPT: {answer}")

# Atraso opcional antes de uma nova requisição
time.sleep(1)  # Espera 1 segundo
