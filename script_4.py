def filter_email_headers(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='replace') as infile, open(output_file, 'w', encoding='utf-8', errors='replace') as outfile:
        lines = infile.readlines()

        # Strings que devem ser mantidas no cabeçalho
        header_keywords = [
            "From:",
            "SendTo:",
            "DeliveredDate:",
            "Subject:",
            "MIME_Version:",
            "$MessageID:"
        ]
        
        # Flags para identificar início e fim do cabeçalho
        in_header = False
        for line in lines:
            # Verifica se é o início de um novo email
            if "$BEGIN_NEW_EMAIL$" in line:
                in_header = True
                outfile.write(line)  # Escreve a linha de início do novo email
                continue

            # Verifica se é o fim do cabeçalho
            if "$END_HEADER$" in line:
                in_header = False
                outfile.write(line)  # Escreve a linha de fim do cabeçalho
                continue

            # Mantém as linhas de cabeçalho com as palavras-chave desejadas
            if in_header:
                if any(line.startswith(keyword) for keyword in header_keywords):
                    outfile.write(line)

            # Escreve o restante das linhas que não estão no cabeçalho
            if not in_header:
                outfile.write(line)

# Configuração dos arquivos de entrada e saída
input_file = 'output_script_3.txt'
output_file = 'output_script_4.txt'

# Chama a função de filtragem
filter_email_headers(input_file, output_file)
