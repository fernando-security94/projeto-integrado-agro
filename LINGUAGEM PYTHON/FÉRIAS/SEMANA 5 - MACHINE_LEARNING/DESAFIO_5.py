'''
🔸 Desafio 5 – Machine Learning Simples (Sexta)
🎯 Contexto:
Você quer prever se uma pessoa compra ou não um produto, com base em idade e salário.

🧠 Você vai treinar:
Pipeline básico de ML com Scikit-Learn

Pré-processamento, treino e avaliação de modelo

💻 Desafio:
Crie um dataset simples com colunas: idade, salario, comprou (0 = não, 1 = sim)

Treine um modelo de classificação (ex.: árvore de decisão)

Avalie o modelo com accuracy e matriz de confusão
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Dados
dados = {
    'idade': [25, 45, 35, 33, 52, 23, 43],
    'salario': [5000, 10000, 7000, 8000, 12000, 4000, 9500],
    'comprou': [0, 1, 1, 1, 1, 0, 1]
}

df = pd.DataFrame(dados)

# Features e target
X = df[['idade', 'salario']]
y = df['comprou']

# Split treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modelo
modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

# Previsão
y_pred = modelo.predict(X_test)

# Avaliação
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Matriz de Confusão:\n', confusion_matrix(y_test, y_pred))
