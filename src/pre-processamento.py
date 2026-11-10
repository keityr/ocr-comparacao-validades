# 1. Importar a biblioteca
from PIL import Image
# 2. Caminho da imagem original
caminho = "imagens-teste/xarope.JPG"
# 3. Abrir a imagem
imagem= Image.open(caminho)
# 4. Converter para tons de cinza
imagem_cinza = imagem.convert("L")
# 5. Salvar a imagem nova
imagem_cinza.save("imagens-teste/xarope-cinza.jpg")
