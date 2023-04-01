import os, dotenv
import json
import openai

import string

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

texto = """
Eu amei essa blusa 
"""
prompt = "Responda em ÚNICA palavra, sendo positivo, negativo ou neutro o sentimento contidono seguinte texto: " + texto

response = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt,
    temperature=0.7,
    max_tokens= 35,
    n=1, 
    stop=None 
)

# Passo 1: Pegando response a resposta 
choices = response["choices"][0] 
data_dict = json.loads(str(choices))
resposta = data_dict['text']

# Passo 2: Remove pontos e vírgulas
tabela_punctuation = str.maketrans('', '', string.punctuation)
frase_sem_pontuacao = resposta.translate(tabela_punctuation)

# Passo 3: Transformando a frase em uma lista com base no espaço entre as palavras
tokens = frase_sem_pontuacao.strip().split()

# Passo 4: Seleção de palavras-chave
palavras_chave = ['neutro', 'positivo', 'negativo']
palavras_selecionadas = [token for token in tokens if token.lower() in palavras_chave]

# Passo 5: Juntar as palavras selecionadas
sentimento = ''.join(palavras_selecionadas)

print(sentimento)