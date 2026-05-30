# Excelente pergunta! 🤓 Essa é exatamente a mentalidade que faz diferença: conectar o que você tá aprendendo com a área que quer atuar — Análise de Dados e AML (Anti-Money Laundering). Bora fazer essa ponte juntos:

# 📊 Aplicação em Análise de Dados
# Imagina que você trabalha com um conjunto de dados de clientes ou transações. Aqueles conceitos básicos que você tá praticando agora (listas, funções, condicionais) vão te ajudar a:

# Limpar os dados (data cleaning)

# Calcular métricas (média de transações, desvio padrão, total gasto)

# Classificar dados (clientes com risco alto/baixo)

# Detectar padrões ou outliers (valores que “fogem do normal”)

# Exemplo simples:
# python
# Copy
# Edit
# transacoes = [1200, 9500, 300, 7500, 15000]

# def calcula_media(valores):
#     return sum(valores) / len(valores)

# media = calcula_media(transacoes)

# for valor in transacoes:
#     if valor > media * 2:  # possível comportamento fora do padrão
#         print(f"Transação suspeita: R${valor}")
# Você tá aplicando a lógica de programação que já conhece para identificar valores incomuns — que é uma base da análise de fraudes/AML.

# 💸 Aplicação em AML (Anti-Money Laundering)
# Agora vamos imaginar uma situação real de AML. Suas ferramentas de trabalho seriam Python, SQL, e ferramentas como Tableau, Power BI, ou até sistemas de AML (Actimize, SAS, etc). Mas no fundo, o que você faz é:

# Exemplo:
# Você tem um arquivo CSV com transações de um banco e quer descobrir se há lavagem de dinheiro.

# Passos típicos:
# Carregar os dados com Python (pandas)

# Filtrar transações suspeitas (valores altos, frequências fora do comum)

# Marcar clientes com comportamento incomum

# Gerar alertas ou visualizações

# python
# Copy
# Edit
# import pandas as pd

# # Leitura de dados de transações
# df = pd.read_csv("transacoes.csv")

# # Exemplo: marcar transações acima de R$ 10.000
# df["suspeita"] = df["valor"] > 10000

# # Contar quantas transações suspeitas por cliente
# suspeitos = df[df["suspeita"]].groupby("cliente_id").count()

# print(suspeitos)
# O que você já aprendeu que se aplica:
# Funções = organizar seu código

# Listas = armazenar registros

# Condicionais = aplicar regras de negócios

# Laços de repetição = percorrer linhas de dados

# 🧠 Conclusão
# Você tá treinando o "musculozinho" certo — a lógica!
# A parte técnica mais pesada 
# (como usar pandas, SQL, bibliotecas de Machine Learning) 
# você vai aprender com o tempo, mas só faz sentido se a lógica estiver sólida — 
# e é isso que você tá fazendo agora.

import pandas as pd
import random
from datetime import datetime, timedelta

# Simular um dataset de transações
clientes = ['C001', 'C002', 'C003', 'C004']
dados = []

for cliente in clientes:
    for i in range(random.randint(5, 10)):
        valor = random.choice([100, 500, 3000, 7500, 10000, 15000, 20000])
        data = datetime(2025, 4, 1) + timedelta(days=random.randint(0, 2), hours=random.randint(0, 23))
        dados.append({'cliente_id': cliente, 'valor': valor, 'data_hora': data})

# Criar DataFrame
df = pd.DataFrame(dados)

# Mostrar as primeiras linhas
print("Transações registradas:")
print(df.head(), "\n")

# 1. Transações suspeitas (valor acima de 10 mil)
df['suspeita_valor'] = df['valor'] > 10000

# 2. Transações repetidas (smurfing simples)
df['trans_duplicada'] = df.duplicated(subset=['cliente_id', 'valor'], keep=False)

# 3. Transações em horários noturnos (ex: entre 0h e 5h)
df['hora'] = df['data_hora'].dt.hour
df['horario_suspeito'] = df['hora'].between(0, 5)

# Mostrar resultados com suspeitas
suspeitas = df[(df['suspeita_valor']) | (df['trans_duplicada']) | (df['horario_suspeito'])]
print("Transações suspeitas encontradas:\n")
print(suspeitas[['cliente_id', 'valor', 'data_hora', 'suspeita_valor', 'trans_duplicada', 'horario_suspeito']])

# Quantidade de alertas por cliente
alertas_por_cliente = suspeitas.groupby("cliente_id").size().reset_index(name="qtd_alertas")
print("\nQuantidade de alertas por cliente:\n")
print(alertas_por_cliente)

# salvando em excel
# suspeitas.to_excel("transacoes_suspeitas.xlsx", index=False)
# print("Arquivo Excel salvo com sucesso!")

# salvando em csv para SQL e Tableau
# suspeitas.to_csv("transacoes_suspeitas.csv", index=False)
# print("Arquivo CSV salvo com sucesso!")

# salvando por alerta de clientes
alertas_por_cliente.to_csv("alertas_por_cliente.csv", index=False)


