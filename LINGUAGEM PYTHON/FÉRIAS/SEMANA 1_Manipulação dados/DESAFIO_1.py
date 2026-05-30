'''🔸 Desafio 1 – Automação com Python (Segunda)
🎯 Contexto:
Você recebeu uma pasta cheia de arquivos .csv de relatórios financeiros. Precisa juntar todos em um único arquivo.

🧠 Você vai treinar:
Manipulação de arquivos e diretórios (os, glob)

Leitura e concatenação de arquivos com Pandas

💻 Desafio:
Crie um script que:

Busque todos os arquivos .csv na pasta relatorios/

Leia cada um e os combine em um único DataFrame

Salve o resultado em um arquivo relatorio_geral.csv
'''

import pandas as pd
import glob
import os

# Definir o caminho da pasta
caminho = './LINGUAGEM PYTHON/FÉRIAS/relatorios'

# Encontrar todos os arquivos CSV
arquivos = glob.glob(os.path.join(caminho, '*.csv')) + glob.glob(os.path.join(caminho, '*.CSV'))

print(f'Arquivos encontrados: {arquivos}')

# Lista para armazenar os DataFrames
dataframes = []

# Loop para ler os arquivos
for arquivo in arquivos:
    df = pd.read_csv(arquivo)
    dataframes.append(df)

# Junta todos
resultado = pd.concat(dataframes)

# Salvar
resultado.to_csv('relatorio_geral.csv', index=False)



# Exemplo de criar exemplos de CSV
'''
import pandas as pd
import os

# Criar a pasta se não existir
os.makedirs('relatorios', exist_ok=True)

# Dados dos meses
dados_janeiro = {
    'id': [1, 2, 3],
    'produto': ['Camiseta', 'Calça', 'Boné'],
    'quantidade': [5, 3, 2],
    'preco_unitario': [50, 100, 30]
}

dados_fevereiro = {
    'id': [4, 5, 6],
    'produto': ['Camiseta', 'Calça', 'Boné'],
    'quantidade': [6, 4, 3],
    'preco_unitario': [50, 100, 30]
}

dados_marco = {
    'id': [7, 8, 9],
    'produto': ['Camiseta', 'Calça', 'Boné'],
    'quantidade': [7, 2, 5],
    'preco_unitario': [50, 100, 30]
}

# Criar DataFrames
df_jan = pd.DataFrame(dados_janeiro)
df_fev = pd.DataFrame(dados_fevereiro)
df_mar = pd.DataFrame(dados_marco)

# Salvar como CSV
df_jan.to_csv('relatorios/vendas_janeiro.csv', index=False)
df_fev.to_csv('relatorios/vendas_fevereiro.csv', index=False)
df_mar.to_csv('relatorios/vendas_marco.csv', index=False)

print('Arquivos CSV criados com sucesso!')




'''