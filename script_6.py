def rename_headers(input_file, output_file):
    # Ler o conteúdo do arquivo de entrada
    with open(input_file, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()

    # Substituir as strings desejadas
    new_lines = []
    for line in lines:
        # Renomear "SendTo:" para "To:"
        if line.startswith("SendTo:"):
            new_lines.append(line.replace("SendTo:", "To:", 1))
        # Renomear "$MessageID:" para "MessageID:"
        elif line.startswith("$MessageID:"):
            new_lines.append(line.replace("$MessageID:", "MessageID:", 1))
        else:
            new_lines.append(line)

    # Salvar o novo conteúdo em um arquivo de saída
    with open(output_file, 'w', encoding='utf-8', errors='replace') as f:
        f.writelines(new_lines)

# Exemplo de uso
input_file = 'output_script_5.txt'
output_file = 'output_script_6.txt'
rename_headers(input_file, output_file)
