import openpyxl 
from PIL import Image, ImageDraw, ImageFont

# Abrir a planilha
workbook_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['Sheet1']

# Iterar sobre as linhas da planilha
for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2)):
    # Informações de cada célula
    nome_curso = linha[0].value
    nome_participante = linha[1].value
    tipo_participacao = linha[2].value

    carga_horaria = linha[5].value
    
    data_inicio = linha[3].value 
    data_final = linha[4].value

    data_emissao = linha[6].value
    # Transferir dados da planilha para a imagem
    fonte_nome = ImageFont.truetype('./tahomabd.ttf', 90)  
    fonte_geral = ImageFont.truetype('./tahoma.ttf', 80)   # Adicionar o tamanho da fonte
    fonte_data = ImageFont.truetype('./tahoma.ttf', 55)   

    # Criar o certificado com as informações
    image = Image.open('./certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(image)

    desenhar.text((1020, 827), nome_participante, fill='black', font=fonte_nome) # Ver coordenadas pelo paint
    desenhar.text((1060, 950), nome_curso, fill='black', font=fonte_geral)
    desenhar.text((1435, 1065), tipo_participacao, fill='black', font=fonte_geral)
    desenhar.text((1480, 1182), str(carga_horaria), fill='black', font=fonte_geral) 

    desenhar.text((750, 1770), data_inicio, fill='blue', font=fonte_data)
    desenhar.text((750, 1930), data_final, fill='blue', font=fonte_data)

    desenhar.text((2220, 1930), data_emissao, fill='blue', font=fonte_data)

    image.save(f'./{indice}_{nome_participante}_certificado.png')
