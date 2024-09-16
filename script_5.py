from datetime import datetime
import pytz

def convert_delivered_date(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='replace') as infile:
        lines = infile.readlines()

    converted_lines = []

    for line in lines:
        if line.startswith("DeliveredDate:"):
            date_str = line[len("DeliveredDate:"):].strip()
            try:
                # Converte a string da data para um objeto datetime no formato correto
                date_obj = datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")

                # Define o fuso horário de Brasília (BRT)
                brt = pytz.timezone('America/Sao_Paulo')
                date_obj_brt = brt.localize(date_obj)

                # Converte para o formato de e-mail, incluindo o fuso horário de Brasília
                formatted_date = date_obj_brt.strftime("%a, %d %b %Y %H:%M:%S %z")

                # Adiciona a linha convertida, agora como "Date:"
                converted_lines.append(f"Date: {formatted_date}\n")
            except ValueError:
                # Em caso de erro na conversão, mantém a linha original
                converted_lines.append(line)
        else:
            # Mantém as outras linhas inalteradas
            converted_lines.append(line)

    # Garante que o arquivo seja gravado com a codificação correta e que os acentos sejam preservados
    with open(output_file, 'w', encoding='utf-8', errors='replace') as outfile:
        outfile.writelines(converted_lines)

# Configuração dos arquivos de entrada e saída
input_file = 'output_script_4.txt'
output_file = 'output_script_5.txt'

# Chama a função de conversão
convert_delivered_date(input_file, output_file)
