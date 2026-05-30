# captura e transformacao de dados HTML de uma pagina web
# nao sera possivel executar o codigo pq
# a pagina do BC esta indisponivel

# exercicio:
# criae data frame com 5 linhas a partir de um dict
# contem nome, quantidade de itens comprados, tipo de item
# receita total

import pandas as pd

# criando dataFrame
data = {
    'Nome':['Produto A','Produto B','Produto C','Produto D', 'Produto E'],
    'Quantidade de itens comprados':[3, 1, 4, 3, 2],
    'Tipo do item':['Eletrônico', 'Vestuário', 'Alimento', 'Eletrônico', 'Alimento'],
    'Receita total':[120, 80, 60, 120, 90]
}

df = pd.DataFrame(data)

# removendo duplicados
df.drop_duplicates(keep='last', inplace=True)

# calcula preco item
df['Preço do item'] = df['Receita total'] / df['Quantidade de itens comprados']

# selecionar itens acima de 50
itens_acima_50 = df[df['Preço do item'] > 50]

print("Preco do item:")
print(df['Preço do item'])
print()
print(f'Itens acima de 50 reais:')
print(itens_acima_50)


