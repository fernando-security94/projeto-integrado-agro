

# Análise Exploratória e Visualização:
# a) Gráfico de Linha para Tendências Anuais de Consumo e Valores:
# Visualize o consumo anual total e os valores médios das faturas.
# b) Gráfico de Barras para Consumo Médio por Mês:
# Avalie padrões sazonais ao longo dos meses.
# c) Análise de Correlação:
# Explore a relação entre consumo e valor da fatura.
# d) Gráfico Interativo com Plotly:
# Crie gráficos interativos para facilitar a exploração dos dados.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import unidecode

# carrregando conjunto de dados
dados = pd.read_excel('d:\Cybersecurity\Market Intelligence and Data Analysis\Programação Orientada a Objeto\consumo de energia')
df = pd.DataFrame(dados)

# Exibir os cabeçalhos
print(df.head())
print()



# Formatação das colunas para evitar possíveis erros
df.columns = df.columns.str.strip()

# exibir colunas
print(df.columns)
print()


# Grafico de linha para tendencia anual de consumo e valores
# Visualizar consumo anual total e valores medios das faturas

# Primeiros vamos agrupar por ano e valor bruto
df_ano = df.groupby('ANO').agg({
    'CONSUMO-KWH': 'sum',
    'VALOR BRUTO DA FATURA': 'mean'
}).reset_index()

# Plotagem dos dados em linha de tendencia
plt.figure(figsize=(10, 6))
plt.plot(df_ano['ANO'], df_ano['CONSUMO-KWH'], label='Consumo Total em KWH', color='green', marker='o')
plt.plot(df_ano['ANO'], df_ano['VALOR BRUTO DA FATURA'], label='Valor Médio da Fatura', color='royalblue', marker='s')
plt.title('Tendência Anual: Consumo x Valor Médio da Fatura')
plt.xlabel('Ano')
plt.ylabel('Consumo / Valor')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



# Manipulação dos dados para criação do gráfico
# de barras que analisa o consumo médio por mese
# Analisar padrões sazonais e variação do consumo ao longo dos meses.
# Caso haja um aumento exponencial no verão, por exemplo, podemos 
# concluir que possivelmente seja devido ao uso de ar-condicionado e/ou
# aquecedor no inverno.

# Checando se a coluna mês existe
print(df['MÊS'].unique())
print()


# Formatando e limpando no dataFrame original
# Padronizar a coluna MÊS na base original antes de qualquer agrupamento
df['MÊS'] = df['MÊS'].astype(str).str.strip().str.upper()
df['MÊS'] = df['MÊS'].apply(unidecode.unidecode)

# Agrupando os dados por mês e calculo do consumo médio em KWH
# similar ao primeiro agrupamento
df_mes = df.groupby('MÊS').agg({'CONSUMO-KWH': 'mean'}).reset_index()


# Aparentemente, os meses estão fora de ordem no terminal
# portanto, vou reorganizar a ordem em uma variável "meses"
meses = ['JANEIRO', 'FEVEREIRO', 'MARCO', 'ABRIL', 'MAIO', 'JUNHO',
'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']

# Garantindo a ordem correta com .sort_values()
df_mes['MÊS'] = pd.Categorical(df_mes['MÊS'], categories=meses, ordered=True)
df_mes = df_mes.sort_values('MÊS')

print(df_mes['MÊS'].unique())
print()


# Parte 2: Plotagem do gráfico de barras com seaborn
plt.figure(figsize=(12, 6))
sns.barplot(data=df_mes, x='MÊS', y='CONSUMO-KWH',  palette='viridis')
plt.xticks(rotation=45)
plt.title('Consumo Médio por Mês em KWH')
plt.xlabel('Mês')
plt.ylabel('Consumo Médio em KWH')
plt.tight_layout()
plt.grid(axis='y')
plt.show()


# Parte 3: Análise de correlação
# Entender se há relação estatística entre o
# consumo de energia e o valor da fatura, entendendo
# se o custo varia proporcionalmente com o uso.

# Seleção das colunas numéricas para analise
df_correlcao = df[['CONSUMO-KWH', 'VALOR BRUTO DA FATURA']]

# calculo da correlação com .corr()
correlation = df_correlcao.corr()

# Exibição da matriz de correlação utilizando
# heatmap()

plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlação entre o Consumo em KWh e Valor da Fatura')
plt.tight_layout()
plt.show()
# 📌 Interpretação: Valores próximos de 1 indicam correlação forte positiva. 
# Perto de 0 significa ausência de relação.



# Parte 4: Plotagem de um grafico interativo com Plotly
# Nesse gráfico, o usuário pode interagir com o 
# gráfico, visualizando valores ao passar o mouse na area
# plotada.

# Criação de nova coluna combinada de ano / mês no eixo X
df['ANO_MÊS'] = df['ANO'].astype(str) + '-' + df['MÊS'].astype(str)

# Plotagem do gráfico
fig = px.line(df, x='ANO_MÊS', y='VALOR BRUTO DA FATURA',
              title='Valor da Fatura ao Longo do Tempo',
              markers=True,
              labels={'VALOR BRUTO DA FATURA': 'Valor (R$)', 'ANO_MÊS': 'Ano-Mês'},
              template='plotly_dark'
)
fig.update_layout(xaxis_tickangle=-45)
# fig.show()


# para abrir no navegador, pois estou usando o Vscode
fig.write_html("grafico_interativo.html", auto_open=True)