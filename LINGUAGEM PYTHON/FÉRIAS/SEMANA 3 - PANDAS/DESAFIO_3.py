'''Desafio 3 – Análise com Pandas e NumPy (Quarta)
🎯 Contexto:
Você recebeu um dataset de notas de alunos. Precisa calcular estatísticas.

🧠 Você vai treinar:
Limpeza de dados

Operações com Pandas e NumPy

💻 Desafio:
Crie um DataFrame com colunas: aluno, prova1, prova2, prova3

Calcule:

Média de cada aluno

Qual foi a maior e menor nota geral

Alunos com média acima de 7
'''

import pandas as pd
import numpy as np

# Criar dados
dados = {
    'aluno': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'prova1': [7.5, 8.0, 5.5, 6.0, 9.0],
    'prova2': [8.5, 7.0, 6.5, 5.0, 8.0],
    'prova3': [9.0, 8.5, 7.0, 6.5, 7.5]
}

df = pd.DataFrame(dados)

# Calcular média
df['media'] = df[['prova1', 'prova2', 'prova3']].mean(axis=1)

print(df)
