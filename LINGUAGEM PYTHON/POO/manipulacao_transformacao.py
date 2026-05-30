# Manipulacao, tranformação e filtragem de dados
# com pandas e numpy

import pandas as pd
import numpy as np

# dados = {
#     'id_cliente': [101, 102, 103, 104],
#     'saldo': [500, 6500, 7000, 800],
#     'tipo_conta': ['corrente', 'poupança', 'corrente', 'corrente']
# }

# df = pd.DataFrame(dados)

# # filtrando o DataFrame pelo tipo de conta
# filtro = df[df['tipo_conta'] == 'poupança']

# print(filtro)
# print()

# # filtrando com loc
# print(df.loc[:3, 'id_cliente'])
# print()

# # filtrando com iloc
# # df.iloc[linha_inicio:linha_fim, coluna_inicio:coluna_fim]
# # começa na linha de indice 1 até o final: começa na coluna de indice 1 até o final
# print(df.iloc[1:, 1:])
# print()

# # começa linha indice 0 ate o final
# # começa coluna indice 0 ate o final
# print(df.iloc[0:, 0:])


# Tratamento de dados nulos
nulos = {
    'id_cliente': [101, 102, 103, 104],
    'saldo': [np.nan, 6500, 7000, 800],
    'tipo_conta': ['corrente', 'poupança', np.nan, 'corrente']
}

df_nulos = pd.DataFrame(nulos)

# identificando nulos com isna()
# retorna True ao encontrar nulos
print(df_nulos.isna())
print()
# tratando nulos com fillna()

df_nulos['saldo'].fillna(0, inplace=True)
print(df_nulos.isna())
print()


df_nulos.fillna({'tipo_conta': 'corrente'}, inplace=True)  # sintaxe para python 3.0
print(df_nulos.isna())
print()


# Agregações com group by e mean()

data = {
    'id_cliente': [101, 102, 103, 104, 105, 106],
    'valor_venda': np.random.randint(100, 200, 6),  # gerar 6 numeros aleatorios entre 100 e 199
    'região': ['Norte', 'Norte', 'Nordeste', 'Nordeste', 'Nordeste', 'Norte']
}

df_data = pd.DataFrame(data)
print(df_data)
print()


# Agrupando por regiões e exibindo média do valor de venda
print(df_data.groupby('região')['valor_venda'].mean())


# Tratando dados com merge() concat()

nomes = {
    'id_cliente': [1, 2, 3, 4],
    'nome': ['João', 'Maria', 'Fernando', 'Poliane']
}

df_nomes = pd.DataFrame(nomes)
print("DataFrame nomes:\n")
print(df_nomes)
print()


vendas = {
    'id_cliente': [1, 2, 3, 4],
    'quantidade_vendida': [100, 150, 200, 250]
}

df_vendas = pd.DataFrame(vendas)
print("DataFrame vendas:\n")
print(df_vendas)
print()

# criando dataframe com merge
df_nomes_vendas = df_nomes.merge(df_vendas)
print("DataFrame nomes_vendas:\n")
print(df_nomes_vendas)
print()


# Concatenando 2 dataframes com concat
nome_venda_nova = {
    'id_cliente': [5],
    'nome': ['Marlos'],
    'quantidade_vendida': [350]
}

df_novo = pd.DataFrame(nome_venda_nova)
print(df_novo)
print()

df_concat = pd.concat([df_nomes_vendas, df_novo])
print("DataFrame concat:\n")
print(df_concat)