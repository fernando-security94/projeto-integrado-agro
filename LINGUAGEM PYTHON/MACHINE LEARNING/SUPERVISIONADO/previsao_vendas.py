# Modelo de previsão para vendas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf

# Criação de dados fictícios de vendas ao longo do tempo
np.random.seed(42)
meses = np.arange(1, 13)
vendas = np.array([200, 220, 250, 280, 300, 320, 350, 380, 400, 420, 450, 480])

# criar um DataFrame
dados = pd.DataFrame({'Mes': meses, 'Vendas': vendas})

# visualização dos dados
plt.scatter(dados['Mes'], dados['Vendas'])
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Dados de Vendas ao Longo do Tempo')
plt.show()


# Divide os dados em conjunto de treinamento e teste

X = dados[['Mes']]
y = dados[['Vendas']]

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalização dos dados de treinamento

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Criar e treinar o modelo de regressão linear com TensorFlow
model = tf.keras.Sequential([

    tf.keras.layers.Input(shape=(1,)),  # Camada de entrada
    tf.keras.layers.Dense(units=8, activation='relu'),   # camada escondida com ativação reLU
    tf.keras.layers.Dense(units=1)  # Camada de saída
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Treinar o modelo por mais epocas
model.fit(X_train, Y_train, epochs=500, verbose=0)

# Previsões no conjunto de teste
predictions = model.predict(X_test)

#Desfazer normalizacao para avaliar o desempenho
min_sales = dados['Vendas'].min()
max_sales = dados['Vendas'].max()


predictions_inverse = predictions * (max_sales - min_sales) + min_sales
y_test_inverse = Y_test * (max_sales - min_sales) + min_sales

# Visualização das previsões em relação aos dados reais
plt.scatter(X_test, y_test_inverse, label='Dados Reais')
plt.plot(X_test, predictions_inverse, color='red', label='Previsões')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Previsão de Vendas com Regressão Linear (TensorFlor)')
plt.legend()
plt.show()

# Avaliar o desempenho do modelo
erro_mse = mean_squared_error(y_test_inverse, predictions_inverse)
print(f'Erro Médio Quadrático (MSE): {erro_mse:.2f}')

# Previsão para o próximo mês
proximo_mes_scaled = scaler.transform(np.array([[13]]))
previsa_prox_mes_sclaed = model.predict(proximo_mes_scaled)
previsao_proximo_mes = scaler.inverse_transform(previsa_prox_mes_sclaed)[0, 0]

print(f'Previsão de Vendas para o Próximo Mês: {previsao_proximo_mes:.2f}')
