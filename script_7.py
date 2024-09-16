import os
import re
from datetime import datetime
import pytz

def extract_and_save_emails(input_file):
    # Verificar se o arquivo de entrada existe
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"O arquivo de entrada {input_file} não foi encontrado.")

    # Obter o diretório do arquivo de entrada
    output_dir = os.path.dirname(input_file)
    
    # Ler o conteúdo do arquivo de entrada
    with open(input_file, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()

    # Definir as strings delimitadoras
    start_marker = "$BEGIN_NEW_EMAIL$"
    end_marker = "$NEW_MAIL_END$"
    
    # Encontrar todos os blocos de email
    email_blocks = content.split(start_marker)[1:]
    email_blocks = [email.split(end_marker)[0] for email in email_blocks]

    # Contador para nomes sequenciais
    counter = 1
    
    for email_block in email_blocks:
        # Extrair a data do campo Date
        match = re.search(r'Date:\s*(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2})', email_block)
        if match:
            date_str = match.group(1)
            # Converter a data para o formato desejado e ajustar o fuso horário
            date = datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
            date = pytz.timezone('America/Sao_Paulo').localize(date)
            file_date = date.strftime('%Y_%m_%d')
        else:
            # Se não encontrar a data, usar uma data padrão
            file_date = '0000_00_00'
        
        # Ordenar os campos do cabeçalho
        header_fields = {
            'From:': None,
            'To:': None,
            'Date:': None,
            'Subject:': None,
            'MIME_Version:': None,
            'MessageID:': None
        }
        
        # Dividir o bloco do email em cabeçalho e corpo
        if '\n\n' in email_block:
            header, body = email_block.split('\n\n', 1)
        else:
            header = email_block
            body = ''
        
        # Processar o cabeçalho
        for line in header.splitlines():
            for key in header_fields:
                if line.startswith(key):
                    header_fields[key] = line
        
        # Reconstituir o cabeçalho em ordem correta
        ordered_header = '\n'.join(header_fields[key] for key in header_fields if header_fields[key] is not None)
        
        # Reconstituir o e-mail com cabeçalho e corpo
        full_email = f"{ordered_header}\n\n{body}"
        
        # Nome do arquivo com numeração sequencial
        output_file = os.path.join(output_dir, f"{file_date}_{counter:03d}.eml")
        
        # Incrementar o contador
        counter += 1
        
        # Salvar o e-mail como um arquivo .eml
        with open(output_file, 'w', encoding='utf-8', errors='replace') as file:
            file.write(full_email)

# Usar o nome do seu arquivo de entrada
input_file = 'output_script_6.txt'
extract_and_save_emails(input_file)



