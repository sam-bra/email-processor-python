def process_emails(input_file, output_file):
    # Ler o conteúdo do arquivo de entrada
    with open(input_file, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()

    # Variáveis para armazenar o novo conteúdo
    new_lines = []
    prev_line = ""

    # Processar linha por linha
    for i, line in enumerate(lines):
        # Adicionar $NEW_MAIL_END$ antes de $BEGIN_NEW_EMAIL$
        if line.strip() == '$BEGIN_NEW_EMAIL$':
            new_lines.append('$NEW_MAIL_END$\n')
        
        # Adicionar a linha atual ao novo conteúdo
        new_lines.append(line)
        
        # Adicionar $END_HEADER$ após DeliveredDate:
        if line.startswith('DeliveredDate:'):
            # Adicionar $END_HEADER$ na linha seguinte
            if i + 1 < len(lines):
                new_lines.append('$END_HEADER$\n')

    # Salvar o novo conteúdo em um arquivo de saída
    with open(output_file, 'w', encoding='utf-8', errors='replace') as f:
        f.writelines(new_lines)

# Exemplo de uso
input_file = 'output_script_2.txt'
output_file = 'output_script_3.txt'
process_emails(input_file, output_file)
