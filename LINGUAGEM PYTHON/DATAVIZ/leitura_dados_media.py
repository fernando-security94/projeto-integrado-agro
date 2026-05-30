# uso de pandas para encontrar a media de idade de um grupo de pessoas

import pandas as pd

dados = {
    'Nome':['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Idade':[25, 30, 22, 35, 28]
}

# cria Serie a partir do dict dados
serie_idades = pd.Series(dados['Idade'], index=dados['Nome'])
media_idades = serie_idades.mean()



print(f'Serie a partir do dict dados: {serie_idades}\n')
print(f'Media de idades: {media_idades}')

print('-' * 50)

# criar dataframe a partir do dict
df = pd.DataFrame(dados)
media_idades_df = df['Idade'].mean()
print('DataFrame:')
print(df,'\n')
print(f'Media de idades em DataFrame: {media_idades_df}')
