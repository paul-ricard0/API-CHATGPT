import os, dotenv
import openai

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_api_answer(nome_produto: str) -> str:
    prompt = f"Gerar uma descrição para se colocar no maketpalce do produto: {nome_produto}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.7,
        max_tokens= 2048,
        n=1, 
        stop=None 
    )
    return response['choices'][0]['text'].strip()

if __name__ == '__main__':
    produto = 'Galaxy buds 2'
    api_answer = get_api_answer(produto)
    print(get_api_answer(api_answer))



