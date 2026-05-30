# exemplo de leitura de dados de uma pagina web
# com url e DataFrame

import pandas as pd
from tabulate import tabulate

# melhora exibicao da tabela
# pd.set_option('display.width', 1000)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', 20)


# variavel que recebe o endereco HTML
url = 'https://www.fdic.gov/bank-failures/failed-bank-list?combine=&items_per_page=All'

# variavel que faz percorre a pagina e subtrai os dados das tabelas
# e aloca em dataFrames
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))

# variavel que recebe os elementos de dfs 
# a partir do primeiro indice
df_bancos = dfs[0]

# exibicao da forma que as colunas da tabela encontrada no link HTML
# estao distribuidas e seus respectivos tipos
print("Table shape: ")
print(df_bancos.shape)
print(df_bancos.dtypes,'\n')

print('-' * 100)

# # exibicao da tabela com a funcao head()
print(df_bancos.head(20))  # posso passar o numero de linhas como argumento

# exibe a tabela com tabulate
#print(tabulate(df_bancos.head(), headers='keys', tablefmt='psql'))

# save to csv
df_bancos.to_csv('bancos.csv', index=False)


