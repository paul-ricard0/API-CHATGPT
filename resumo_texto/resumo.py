import os, dotenv
import openai

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def get_api_answer(text: str) -> str:
    prompt = f"Resuma o seguinte texto: {text}"
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
    file = r'resumo_texto\resumo.txt'
    texto = read_file(file)
    api_answer = get_api_answer(texto)
    print(get_api_answer(api_answer))