# Importar bibliotecas necessárias
import openpyxl 
from PIL import Image, ImageDraw, ImageFont

# Abrir a planilha
workbook_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['Sheet1']

# Iterar sobre as linhas da planilha
for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2, max_row=3)):
    # Informações de cada célula
    nome_curso = linha[0].value
    nome_participante = linha[1].value
    tipo_participacao = linha[2].value
    carga_horaria = linha[5].value

    data_inicio = linha[3].value
    data_final = linha[4].value

    data_emissao = linha[6].value
    input('')

    # Transferir dados da planilha para a imagem
    fonte_nome = ImageFont.truetype('./tahomabd.ttf', 90)  # Adicionei o tamanho da fonte
    fonte_geral = ImageFont.truetype('./tahoma.ttf', 60)   # Adicionei o tamanho da fonte

    image = Image.open('./certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(image)

    desenhar.text((1020, 830), nome_participante, fill='black', font=fonte_nome)
    desenhar.text((1060, 950), nome_curso, fill='black', font=fonte_geral)
    desenhar.text((1435, 1065), tipo_participacao, fill='black', font=fonte_geral)


    image.save(f'./{indice}_{nome_participante}_teste.png')
