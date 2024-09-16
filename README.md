# Email Processor Lotus Notes to .EML using Python

Este projeto processa e-mails exportados em lote do antigo **Lotus Notes**, originalmente em arquivos .TXT, para o formato .EML.

## Descrição

A sequência de scripts ajusta a codificação, formata o cabeçalho e realiza outras operações para preparar os e-mails no formato .eml. A execução dos scripts é feita em etapas, e cada parte do processo é registrada no terminal para facilitar o acompanhamento da execução.

Funcionalidades
- Detecção da codificação do arquivo: Detecta a codificação (ex: UTF-8, ISO-8859-1) do arquivo de e-mail.
- Transformação de codificação ISO-8859-1 para UTF-8: Converte arquivos de e-mail de ISO-8859-1 para UTF-8, preservando os acentos e caracteres especiais.
- Adição de strings ao cabeçalho e corpo do e-mail: Insere identificadores específicos no cabeçalho e corpo para segmentação e formatação adequada.
- Limpeza de cabeçalhos: Remove informações não essenciais dos cabeçalhos dos e-mails.
- Ajuste de data e fuso horário: Ajusta a data, hora e fuso dos e-mails para o formato padrão .eml.
- Renomeação de campos no cabeçalho: Ajusta os campos do cabeçalho para os nomes corretos e ordena conforme o padrão .eml.
- Geração de arquivos .eml individuais: Exporta os e-mails processados como arquivos .eml.

:warning: **IMPORTANTE** :warning:

***Para iniciar o projeto, eu analisei os arquivos originais brutos .TXT que haviam sido exportados do Lotus Notes buscando padrões de campos relevantes dentro dos cabeçalhos dos emails originais para posteriormente utilizá-los na conversão do texto para .EML. Isso pode ser visualizado na dinâmica dos scripts.***

***Para utilizar no seu próprio projeto, você provavelmente terá que ajustar esses campos, mas a lógica é a mesma.*** 


## Como instalar

1. Clone este repositório:

```git clone https://github.com/sam_bra/email-processor-python.git```


2. Instale as dependências:

```pip install -r requirements.txt```


## Como usar

Execute os scripts individualmente ou use o script principal `go.py` para automatizar todos os passos:

```python go.py```


## Estrutura do projeto
- detect_encoding.py: Detecta a codificação de um arquivo. Importante para manter os caracteres especiais é a conversão da codificação para UTF-8. No meu caso os arquivos originais estavam em codificação ISO-8859-1.
- script_1.py: Converte a codificação de ISO-8859-1 para UTF-8.
- script_2.py: Adiciona strings para identificar o cabeçalho.
- script_3.py: Adiciona strings para identificar o corpo do e-mail.
- script_4.py: Remove cabeçalhos de informação desnecessária.
- script_5.py: Ajusta data e fuso horário.
- script_6.py: Renomeia campos do cabeçalho conforme o padrão .eml.
- script_7.py: Ordena os campos do cabeçalho e exporta os e-mails em arquivos .eml.
- go.py: Script principal que executa todas as etapas e coordena o fluxo de execução.


## Bibliotecas 

As bibliotecas usadas no seu projeto incluem tanto bibliotecas padrão do Python quanto uma externa para detecção de codificação. Aqui estão as que você usou:

### Bibliotecas padrão do Python:

- subprocess: Usada para executar os scripts individualmente e monitorar seu progresso.
- datetime: Usada para manipulação e formatação de datas.
- pytz: Usada para lidar com fusos horários.
- unicodedata: Usada para normalizar e remover acentos e caracteres especiais.

#### Biblioteca externa:
- chardet: Usada para detectar a codificação de arquivos. Esta biblioteca precisa ser instalada separadamente, pois não faz parte do Python padrão.

#### Instalação de bibliotecas
A maioria das bibliotecas já vem com o Python. Apenas o chardet e pytz eu precisei instalar manualmente. Use o arquivo requirements.txt para instalar todas.

```pip install -r requirements.txt```

## Licença
Este projeto está licenciado sob a Licença MIT - 2024.
Foram utilizadas ferramentas de IA Generativo neste projeto: ChatGPT.
