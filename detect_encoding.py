import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        print(f"Codificação detectada: {result['encoding']} com confiança {result['confidence']}")

# Exemplo de uso
file_path = 'seu_arquivo_de_emails.txt'
detect_encoding(file_path)
