# 1. Importar a biblioteca
import easyocr
import os
import time
# 2. Caminho da imagem
caminho_base= "imagens-teste/"
leitor = easyocr.Reader(["pt"])

for caminho in os.listdir(caminho_base):
    caminho_imagem = os.path.join(caminho_base,caminho)
    nome_imagem = caminho


    inicio_processamento = time.time()

    # 4. Ler a imagem
    ler_imagem = leitor.readtext(caminho_imagem)
    fim_processamento = time.time()
    tempo_resposta_easyocr = fim_processamento - inicio_processamento
    print(f'Nome da imagem: {nome_imagem}')
    # 5. Mostrar o resultado
    for item in ler_imagem:  

        print(f"Resultado: {item[1]}, Confiança:{item[2]:.2f}")


    print(f"Tempo de resposta do EasyOCR: {tempo_resposta_easyocr:.2f} segundos")
    print('\n')
    print('_'* 50)