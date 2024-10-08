import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Carregar a chave da API do arquivo .env
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("A chave da API do Groq não foi encontrada. Verifique seu arquivo .env.")

client = Groq(api_key=api_key)

def minha_pergunta(pergunta: str):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": pergunta,
                }
            ],
            model="llama3-8b-8192",
        )
        
        #print(chat_completion)  # Para depuração, imprime a resposta completa
        
        # Acesse o texto correto aqui
        return (chat_completion.choices[0].message.content)  # Ajuste o acesso aqui, se necessário
    except Exception as e:
        return f"Ocorreu um erro: {e}"

pergunta = "Quanto faturei ontem?"
resposta = minha_pergunta(pergunta)
print(resposta)
