def convert_to_utf8(input_file, output_file):
    # Abre o arquivo de entrada com a codificação original (ISO-8859-1)
    with open(input_file, 'r', encoding='ISO-8859-1') as infile:
        content = infile.read()
    
    # Salva o conteúdo no arquivo de saída com a codificação UTF-8
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

# Configuração dos arquivos de entrada e saída
input_file = 'original_01.txt'
output_file = 'output_script_1.txt'

# Chama a função de conversão
convert_to_utf8(input_file, output_file)
