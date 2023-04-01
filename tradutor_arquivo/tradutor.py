import os, dotenv
import openai

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    
def write_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
        
def translate(text: str, source_lang: str, target_lang: str) -> str:
    prompt = f"""
    Traduza esse texto em {source_lang} para {target_lang}: {text}
    """
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
    source_lang = 'Inglês'
    source_file = r'tradutor_arquivo\texto_en.txt'

    target_lang = 'Português'
    target_file = r'tradutor_arquivo\texto_pt.txt'

    text = read_file(source_file)
    translation = translate(text, source_lang=source_lang, target_lang=target_lang)

    write_file(translation, file_path=target_file)

    print(translation)