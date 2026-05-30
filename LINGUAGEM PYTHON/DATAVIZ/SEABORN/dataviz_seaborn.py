# exemplo usando biblioteca seaborn

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# carregando dataset tips e stilo do grafico
sns.set(style='whitegrid')
df_tips = sns.load_dataset('tips')
print(df_tips)

# criando grafico
# fig, ax = plt.subplots(1, 3, figsize=(15,5))
# sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])
# sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)
# sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)
# plt.show()


# criando grafico de gastos por periodo
plt.figure(figsize=(8,5))
sns.barplot(x='time', y='total_bill', data=df_tips, hue='sex', estimator=sum, errorbar=None, palette="Set2")
plt.xlabel('Periodo(Time)')
plt.ylabel("Total Gastos")
plt.title('Gastos Totais por Periodo (Almoço e Jantar)')


# Gasto medio por periodo
plt.figure(figsize=(8,5))

# se nao tiver estimator=sum, será a média automaticamente, mean() por padrao
sns.barplot(x='time', y='total_bill', hue='sex', data=df_tips) 
plt.xlabel('Periodo(Time)')
plt.ylabel('Média dos Gastos')
plt.title('Média dos Gastos por Periodo (Almoço e Jantar)')


# media de gorjeta por periodo
'''plt.figure(figsize=(8,5))
sns.barplot(x='time', y='tip',hue='sex', data=df_tips,  palette='Set3')
plt.xlabel('Periodo(Time)')
plt.ylabel('Média de Gorjeta')
plt.title('Média de Gorjeta por Período(Almoço e Jantar)')
plt.show()
'''

# Total de tip por periodo em comparação com sexo
plt.figure(figsize=(8,5))
sns.barplot(x='time', y='tip',hue='sex', data=df_tips,estimator=sum, errorbar=None,  palette='Set3')
plt.xlabel('Periodo(Time)')
plt.ylabel('Gorjeta por Sexo')
plt.title('Total de Gorjeta por Período( Almoço e Jantar) e Sexo')



# criar figura com 3 colunas
plt.figure(figsize=(18,5))

# media de tip por periodo e sexo com barplot
# plt.subplot(n_linhas, n_colunas, índice)

'''
1 = número de linhas → só uma linha de gráficos

3 = número de colunas → três gráficos lado a lado

1 = posição onde será desenhado o gráfico atual

1 = esquerda
2 = meio
3 = direita
'''
plt.subplot(1, 3, 1)
sns.barplot(x='time', y='tip', hue='sex', data=df_tips, palette='Set2')
plt.title('Gorjeta média por período e Sexo')
plt.xlabel('Período')
plt.ylabel('Gorjeta')


# Grafico 2 com boxplot Distribuiçao de gorjetas por dia
plt.subplot(1, 3, 2)
sns.boxplot(x='day', y='tip', data=df_tips, palette='Pastel1')
plt.title("Distribuição das Gorjetas por Dia")
plt.xlabel('Dia da Semana')
plt.ylabel('Gorjeta')


# Grafico 3 com countplot - Numero de clientes por periodo
plt.subplot(1, 3, 3)
sns.countplot(x='time', data=df_tips, palette='Set3')
plt.title('Número de Clientes por Período')
plt.xlabel('Período')

# ajuste de layout e salvamento de imagem
plt.tight_layout()
plt.savefig('Dashboard_tips.png', dpi=300, bbox_inches='tight')
plt.show()




# salvamento automático dos gráficos com plt.savefig

'''plt.savefig('.png', dpi=300, bbox_inches='tight')'''

# salvar em csv
df_tips.to_csv('tips_dataset_tratado.csv', index=False)



''''

✅ Pra ver as colunas que existem no DataFrame df_tips, o jeito mais simples e correto é:
python
Copy
Edit
print(df_tips.columns)
Ou, se quiser uma visualização ainda mais amigável:

python
Copy
Edit
print(df_tips.head())   # mostra as primeiras 5 linhas com os nomes das colunas
🧠 Extra: se quiser algo mais detalhado ainda
python
Copy
Edit
df_tips.info()
Isso vai te mostrar:

nomes das colunas

tipos de dados (object, float64, etc.)

quantos valores nulos existem em cada coluna

🤓 Recapitulando:
Não precisa usar pd.DataFrame(df_tips) — 
isso é usado quando você tem dados crus (como listas, dicionários ou arrays) 
e quer criar um DataFrame do zero.

df_tips já é um DataFrame, carregado direto com sns.load_dataset('tips').




'''