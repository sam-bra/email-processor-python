Automação de Processamento de E-mails em Lote

Descrição
Este projeto em Python automatiza o processamento de arquivos de e-mail em lote, realizando diversas transformações e ajustes nos e-mails, convertendo a codificação de caracteres, formatando cabeçalhos, e ajustando datas para o padrão de e-mails .eml. A execução dos scripts é feita em etapas, e cada parte do processo é registrada no terminal para facilitar o acompanhamento da execução.

Funcionalidades
Transformação de codificação ISO-8859-1 para UTF-8: Converte arquivos de e-mail de ISO-8859-1 para UTF-8, preservando os acentos e caracteres especiais.
Adição de strings ao cabeçalho e corpo do e-mail: Insere identificadores específicos no cabeçalho e corpo para segmentação e formatação adequada.
Limpeza de cabeçalhos: Remove informações não essenciais dos cabeçalhos dos e-mails.
Ajuste de data e fuso horário: Ajusta a data, hora e fuso dos e-mails para o formato padrão .eml.
Renomeação de campos no cabeçalho: Ajusta os campos do cabeçalho para os nomes corretos e ordena conforme o padrão .eml.
Geração de arquivos .eml individuais: Exporta os e-mails processados como arquivos .eml.

Antes de iniciar instalar o chardet para verificar se a codificação dos seus arquivos é ISO-8859-1.

C:\>  pip install chardet

Dentro do PYTHON executar

"
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read(10000)  # Ler uma parte do arquivo para detectar a codificação
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    confidence = result['confidence']
    return encoding, confidence

# Configuração do arquivo
file_path = 'original_01.txt'
encoding, confidence = detect_encoding(file_path)
print(f'Codificação detectada: {encoding} com confiança {confidence}')
"

Se for ISO-8859-1 pode continuar. Se não for, altere o "script_1.py".


