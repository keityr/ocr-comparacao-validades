# 1. Importar as bibliotecas
import requests   # faz requisições HTTP (conversa com a API)
import base64     # converte a imagem em texto
import time       # cronômetro
import os

# 2. Definir a URL da API do Ollama
url = "http://localhost:11434/api/generate"

caminho_base = "imagens-teste/"
# 3. Definir o caminho da imagem
for caminho in os.listdir(caminho_base):
    arquivo = caminho.lower()
    if not arquivo.endswith((".png", ".jpg")):
        continue
    caminho_imagem = os.path.join(caminho_base, caminho)


# 4. Ler a imagem e converter para base64
# "rb" = abrir para leitura (r) em modo binário (b), porque imagem não é texto

    with open(caminho_imagem, "rb") as arquivo:
        conteudo = arquivo.read()                                  # lê os bytes da imagem
        imagem_base64 = base64.b64encode(conteudo).decode("utf-8") # bytes -> base64 -> texto

    # 5. Montar os dados da requisição (um dicionário)
    dados = {
        "model": "glm-ocr",              # qual modelo usar
        "prompt": "Text Recognition:",   # a instrução
        "images": [imagem_base64],       # lista com a imagem em base64
        "stream": False                  # resposta inteira de uma vez
    }

    # 6. Enviar a requisição (e cronometrar)
    inicio = time.time()
    resposta = requests.post(url, json=dados)
    fim = time.time()

    # 7. Checar se deu certo
    if resposta.status_code != 200:
        print(f"Erro na requisição: {resposta.status_code}")
        print(resposta.text)
    else:
        # 8. Pegar o texto da resposta
        resultado = resposta.json()        # transforma o JSON em dicionário
        texto = resultado["response"]      # pega só o campo com o texto lido

        # 9. Mostrar o resultado
        print(f"Imagem: {caminho_imagem}")
        print(f"Retorno do GLM-OCR:\n{texto}")
        print(f"Tempo de resposta do GLM-OCR: {fim - inicio:.2f} segundos")