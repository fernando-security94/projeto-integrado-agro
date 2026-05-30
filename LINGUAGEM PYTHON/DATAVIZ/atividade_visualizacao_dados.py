'''''
ATIVIDADE PROPOSTA:
Você trabalha em uma empresa de varejo e precisa 
analisar os dados de vendas do último ano para identificar padrões 
e insights para melhorar o desempenho. Os dados estão armazenados
em um banco de dados SQLite, e você utilizará 
a biblioteca Pandas para manipular e analisar esses dados,
além de gerar visualizações utilizando Matplotlib e Seaborn.'''


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# conectar ao banco de dados ou criar se nao existit
# criar cursor que percorre o banco de dados
conn = sqlite3.connect('dados_vendas.db')
cursor = conn.cursor()

# Criar tabela no banco de dados(se nao existir)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas1(
        id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
        data_venda DATE,
        produto TEXT,
        categoria TEXT,
        valor_venda REAL               

)
               
''')

# Inserção de dados na tabela através de uma lista
# que será integrada com a função .executemany()

vendas = [
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00)]

"""
Se a tabela já tiver dados, você não insere de novo.
Se o banco estiver vazio, você insere automaticamente.
Os gráficos sempre terão dados para funcionar.
"""
# criando um laço condicional que nao insere os mesmos
# dados a cada teste
cursor.execute('SELECT COUNT(*) FROM vendas1')
quantidade = cursor.fetchone()[0]


# Inserção da lista de dados com .executemany()
if quantidade == 0:
    cursor.executemany('''
    INSERT INTO vendas1(data_venda, produto, categoria, valor_venda)
    VALUES(?,?,?,?)

    ''', vendas)
    conn.commit()

    print("Dados inseridos com sucesso")
else:
    print('Dados não inseridos. ERROR: DADOS JÁ EXISTENTES!')

print()


# leitura dos dados com pandas e criaçao do DataFrame
df_vendas = pd.read_sql("SELECT * FROM vendas1", conn)

print(df_vendas)

# fechar conexao com banco de dados
conn.close()


# criando as visualizações de dados com matplotlib e seaborn

# Gráfico 1: Vendas por categoria (gráfico em barra)
# selecionei o estimator=sum para retornar a soma das vendas
# por categoria. Utilizei pallete="pastel" por serem
# cores mais suaves
plt.figure(figsize=(8, 5))
sns.barplot(x='categoria', y='valor_venda', data=df_vendas, estimator=sum,hue='categoria', errorbar=None, palette="pastel")
plt.title('Total de Vendas por Categoria em 2023')
plt.xlabel('Categoria')
plt.ylabel('Valor Total de Vendas em R$')
plt.tight_layout()
plt.show()


# Gráfico 2: Vendas ao longo dos meses (gráfico de linhas)
# Para isso, será necessário transformar a coluna data
# em tipo DATE
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])

# Ordenar por datas através da função sort_values()
df_vendas = df_vendas.sort_values('data_venda')

# Criação do gráfico
plt.figure(figsize=(12, 6))
sns.barplot(x='data_venda', y='valor_venda', data=df_vendas, color="royalblue")
plt.title('Vendas no Ano de 2023')
plt.xlabel('Data da venda')
plt.ylabel('Valor da venda em R$')

# formatacao visual
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Criação de gráfico em linha para observar tendencia:
# Criação do gráfico
plt.figure(figsize=(12, 6))
sns.lineplot(x='data_venda', y='valor_venda', data=df_vendas, marker='o', color="royalblue")
plt.title('Vendas no Ano de 2023')
plt.xlabel('Data da venda')
plt.ylabel('Valor da venda em R$')

# formatacao visual
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# extração do mes da coluna data para agrupar
# as vendas por mes
df_vendas['mes'] = df_vendas['data_venda'].dt.month

# agrupar o total de vendas por mes
vendas_por_mes = df_vendas.groupby('mes')['valor_venda'].sum().reset_index()

# grafico 3
# criacao do grafico de linha baseado no 
# groupby() mensal
plt.figure(figsize=(10,6))
sns.lineplot(x='mes', y='valor_venda', data=vendas_por_mes, marker='o', color="seagreen")
plt.title('Total de Vendas por Mês em 2023')
plt.xlabel('Mês')
plt.ylabel("Valor Total de Vendas em R$")
plt.xticks(ticks=range(1,13), labels=[
    'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
    'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'
])
plt.grid(True)
plt.tight_layout()
plt.show()


# criando um dataviz com os tres graficos
# atraves de plt.subplot()

# extrair mes novamente, por garantia
df_vendas['mes'] = df_vendas['data_venda'].dt.month

# agrupamento por mes e valor total de venda
vendas_por_mes = df_vendas.groupby('mes')['valor_venda'].sum().reset_index()
vendas_por_categoria = df_vendas.groupby('categoria')['valor_venda'].sum().reset_index()

# criação dos comparativos
# tamanho da figura para nao fcar apertado
plt.figure(figsize=(18,6))

# Grafico 1: Barras por categoria
plt.subplot(1,3, 1)
sns.barplot(x='categoria', y='valor_venda', data=vendas_por_categoria, palette="pastel")
plt.title("Total de Vendas por Categoria")
plt.xlabel('Categoria')
plt.ylabel('Venda em R$')
plt.xticks(rotation=45)

# Gráfico 2: Barras por mês
plt.subplot(1, 3, 2)
sns.barplot(x='mes', y='valor_venda', data=vendas_por_mes, palette="Blues_d")
plt.title('Total de Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel("Vendas em R$")
plt.xticks(ticks=range(0, 12), labels=[
    'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
    'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'
])

# Grafico 3: Linha de tendencia por mes
plt.subplot(1, 3, 3)
sns.lineplot(x='mes', y='valor_venda', data=vendas_por_mes, marker='o', color="seagreen")
plt.title("Tendência de Vendas por Mês")
plt.xlabel('Mês')
plt.ylabel('Vendas em R$')
plt.xticks(ticks=range(1, 13), labels=[
    'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
    'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'
])

plt.grid(True)

# Ajuste de layout para nao se sobreporem
plt.tight_layout()
plt.show()



# Analisando os dados:
# Organizando pela categoria que mais faturou

print("Categoria com maior faturamento:\n")
print(df_vendas.groupby('categoria')['valor_venda'].sum().sort_values(ascending=False))
print()

# Exibindo o mês com maior venda:
# Primeiro vamos extrair o mês
df_vendas['mes'] = df_vendas['data_venda'].dt.month

# agrupar os valores das vendas por meses
vendas_por_mes = df_vendas.groupby('mes')['valor_venda'].sum()

# Exibir os valores agrupados
# ascending=False para exibir do maior para o menor
print("Vendas por mes:\n")
print(vendas_por_mes.sort_values(ascending=False))








"""
Análise e Insights dos Dados de Vendas (2023)
Após análise dos dados de vendas de 2023,
 alguns padrões importantes foram identificados:

Categoria de maior faturamento:
A categoria Eletrônicos liderou o volume de vendas, representando a maior fatia do faturamento total da empresa.

Picos de vendas:
Observamos aumentos significativos nas vendas nos meses de janeiro e novembro, o que pode estar relacionado a eventos como liquidações de início de ano e promoções da Black Friday.

Produtos mais vendidos:
Produtos de alto valor agregado, como os da linha de eletrônicos, foram os responsáveis pelos maiores valores individuais de venda.

Sugestões estratégicas:

Investir mais em campanhas promocionais voltadas para eletrônicos.

Preparar estoques reforçados para o início e o final do ano.

Explorar promoções de livros e roupas nos meses de menor venda para estimular a movimentação.

Esses insights podem ajudar a empresa a planejar melhor suas ações de marketing, 
estoque e vendas para o próximo ano, 
maximizando o faturamento em períodos estratégicos.
"Utilizamos um gráfico de linha para representar a evolução das vendas ao longo do ano de 2023. 
Esse formato permite visualizar de forma clara os momentos de crescimento 
e queda nas vendas, facilitando a identificação de tendências sazonais e períodos de maior movimento."
"""

"""
Comando	O que faz
dt.month	Extrai apenas o mês da data

groupby('mes')['valor_venda'].sum()	Soma todas as vendas de cada mês

.reset_index()	Gera um novo DataFrame limpinho para plotar

marker='o'	Destaca cada mês com um pontinho

xticks	Troca os números (1,2,3) por nomes ('Jan', 'Fev', etc.)



"""