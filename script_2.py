def add_new_email_marker(input_file, output_file):
    # Ler o conteúdo do arquivo de entrada
    with open(input_file, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()

    # Variáveis para armazenar o novo conteúdo e estado
    new_lines = []
    blank_lines = 0
    marker_added = False

    # Adicionar o marcador $BEGIN_NEW_EMAIL$ na primeira linha
    new_lines.append('$BEGIN_NEW_EMAIL$\n')

    # Processar linha por linha
    for i, line in enumerate(lines):
        # Contar linhas em branco
        if line.strip() == '':
            blank_lines += 1
        else:
            if blank_lines >= 2 and not marker_added:
                # Verificar se a linha seguinte começa com "Received:"
                if i < len(lines) - 1 and lines[i + 1].startswith('Received:'):
                    # Adicionar o marcador na linha anterior ao "Received:"
                    new_lines.append('$BEGIN_NEW_EMAIL$\n')
                    marker_added = True
            # Resetar o contador de linhas em branco
            blank_lines = 0
            marker_added = False

        # Adicionar a linha atual ao novo conteúdo
        new_lines.append(line)

    # Salvar o novo conteúdo em um arquivo de saída
    with open(output_file, 'w', encoding='utf-8', errors='replace') as f:
        f.writelines(new_lines)

# Exemplo de uso
input_file = 'output_script_1.txt'
output_file = 'output_script_2.txt'
add_new_email_marker(input_file, output_file)
