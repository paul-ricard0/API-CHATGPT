import os, dotenv
import openai
import subprocess

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_comando(texto: str) -> str:
    prompt = f"""
    Me retorne a penas o comando cmd que faça o seguinte: {texto}
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

def __executar_comando_shell(comando: str) -> None:
    try:
        resultado = subprocess.run(comando, shell=True, check=True)
        print(resultado)
    except subprocess.CalledProcessError as e:
        print(e)
        
def validar_comando(comando: str) -> str:
    print(f'Comando gerado: {comando}')
    validacao = input('Seguir com comando: (y/n) ') 
    
    if validacao.upper() == 'Y' or validacao.upper() == 'YES':
        __executar_comando_shell(comando) 
        
    return 'Execução do comando encerrada'
        
if __name__ == '__main__':       
    descricao_comando = input('Digite uma descrição para o comando shell: ')

    comando = gerar_comando(descricao_comando)

    validar_comando(comando)