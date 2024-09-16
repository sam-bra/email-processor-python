import subprocess

def run_script(script_name, part_number, description):
    print(f"Começando a parte {part_number}: {description}")
    
    try:
        # Executa o script e aguarda sua conclusão
        result = subprocess.run(['python', script_name], check=True)
        
        # Se o script foi executado com sucesso, imprime a mensagem
        print(f"Parte {part_number} ({description}) finalizada com sucesso.\n")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar a parte {part_number}: {description}")
        print(f"Erro: {e}\n")

# Lista de scripts e suas etapas com descrições
scripts = [
    ('script_1.py', 1, 'Transformando ISO-8859-1 em UTF-8'),
    ('script_2.py', 2, 'Adicionando strings para o cabeçalho'),
    ('script_3.py', 3, 'Adicionando strings para o corpo do email'),
    ('script_4.py', 4, 'Limpando cabeçalhos de informação não essencial'),
    ('script_5.py', 5, 'Ajustando data, hora e fuso para padrão do formato EML'),
    ('script_6.py', 6, 'Ajustando nomes dos campos padrão do formato EML'),
    ('script_7.py', 7, 'Ajustando ordem do cabeçalho para padrão EML e exportando emails individuais EML'),

   # Adicione mais scripts aqui com títulos descritivos

]

# Executa cada script na ordem
for script, part_number, description in scripts:
    run_script(script, part_number, description)

print("Todos os scripts foram executados com sucesso!")
