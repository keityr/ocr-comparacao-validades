# 1. Importar a biblioteca
from PIL import Image
import pytesseract
import os 
import time
#2.Definir o caminho da imagem
caminho_base = "imagens-teste/"
for caminho in os.listdir(caminho_base):
    arquivo = caminho
    caminho_imagem = os.path.join(caminho_base, caminho)

    #3. Guarda a imagem
    imagem = Image.open(caminho_imagem)
    
    #5.Tempo de resposta do Tesseract
    tempo_resposta_tesseract = time.time()

    #4.Tranformar imagem em texto com tesseract
    texto_extraido = pytesseract.image_to_string(imagem, lang="por")

  

    6# Imprimir resposta do Tesseract
    print(f'Nome da imagem a ser processada {arquivo}:\n'

    f'Retorno do Tesseract:\n {texto_extraido}')


    # Final da resposta do Tesseract em segundos
    fim_resposta_tesseract = time.time()
    print("\n")
    print(f'Tempo de resposta do Tesseract: {fim_resposta_tesseract - tempo_resposta_tesseract:.2f}')
    print("\n")
    print( '_' * 50)
    
    
    