# Exemplo de treinamento supervisionado 
# para machine learning

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import Input

# Dados de treinamento
# X_train representa as entradas e 
# Y_train representa as saídas dobradas
X_train = tf.constant([[1.0], [2.0], [3.0], [4.0], [5.0]])
Y_train = tf.constant([[2.0], [4.0], [6.0], [8.0], [10.0]])



# Criação do modelos com entrada explicita
model = Sequential([
    Input(shape=(1,)),  # define a entrada explicitamente
    Dense(units=1)      # camada densa. Saida com 1 neuronio (Regressao linear simples)
])

# compilação do modelos
model.compile(optimizer='sgd', loss='mean_squared_error')

# treinamento do modelo
model.fit(X_train, Y_train, epochs=1000, verbose=0)


# Previsão para novo valor
X_new = tf.constant([[7.0]])
prediction_x = model.predict(X_new)
print("Predição para entrada 5.0:", prediction_x[0][0])


# Faixa de valores para desenhar a linha de regressão
X_range = np.linspace(0, 6, 100).reshape(-1, 1)
Y_pred_range = model.predict(X_range)


# exibição de dados do modelo
plt.scatter(X_train, Y_train, color='royalblue', label='Dados de Treino')
plt.plot(X_range,Y_pred_range, color='red', label='Previsão do Modelo')
plt.xlabel('Entrada')
plt.ylabel('Saída')
plt.title('Regressão Linear com TensorFlow')
plt.legend()
plt.grid(True)
plt.show()

"""
Principais correções feitas:
✅ model.fit(...) vem antes das previsões.

✅ Corrigido o plt.plot(...) com as previsões após o treinamento.

✅ Removido argumento inválido no plt.plot(...) que causava erro.

✅ Inclusão de print() claro para mostrar a predição.




"""


"""
✅ O que o script faz:
Importações:

matplotlib.pyplot para visualização.

tensorflow e suas APIs de Keras para construção e 
treinamento do modelo.

Dados de treino:

X_train: Entradas (1, 2, 3, 4).

Y_train: Saídas esperadas (2, 4, 6, 8) — ou seja, cada y é o dobro de x.

Modelo de regressão linear:

Sequential(): Modelo linear com uma camada densa (Dense) de 1 unidade.

input_shape=(1,): A entrada tem uma dimensão (um único número por amostra).

optimizer='sgd': Usa gradiente descendente (stochastic gradient descent).

loss='mean_squared_error': Erro quadrático médio como função de perda.

Treinamento:

epochs=1000: O modelo “vê” os dados 1000 vezes para aprender.

Predição:

O modelo prevê a saída correspondente para x = 5.0.

Plotagem:

Embora você chame plt.ylabel('Notas'), nada é plotado, pois não há plt.plot() nem plt.xlabel().




"""


"""
Passo a passo do codigo:
1 - NumPy e Matplotlib: usados para gerar e visualizar os dados.
TensorFlow: usado para criar
e treinar o modelo de aprendizado de máquina.

2. Criação dos dados

X_train = tf.constant([[1.0], [2.0], [3.0], [4.0]])
Y_train = tf.constant([[2.0], [4.0], [6.0], [8.0]])
Dados simples: cada Y é exatamente 2 * X — essa é a função que o modelo precisa aprender.


3. Criação do modelo

model = Sequential([
    Input(shape=(1,)),
    Dense(units=1)
])
Um modelo Sequential com:
Uma camada de entrada com 1 neurônio (porque temos 1 variável de entrada).
Uma camada Dense com 1 unidade (neurônio), que fará a multiplicação + viés: Y = W*X + b.


✅ 4. Compilação

model.compile(optimizer='sgd', loss='mean_squared_error')
Otimizador: sgd (gradiente descendente estocástico), que ajusta os pesos W e b.
Função de perda: erro quadrático médio, ideal para regressão.

Treinamento do modelo

model.fit(X_train, Y_train, epochs=1000, verbose=0)
O modelo passa pelos dados 1000 vezes (épocas), 
ajustando os pesos para minimizar o erro entre Y_pred e Y_real.


7. Fazendo uma nova previsão

X_new = tf.constant([[5.0]])
prediction = model.predict(X_new)
Agora que o modelo está treinado, ele deve prever algo próximo de 10.0.


8. Visualização

plt.scatter(X_train, Y_train, ...)
plt.plot(X_range, Y_pred_range, ...)  # ⚠️ erro aqui também: Y_pred_range foi calculado antes do treinamento
Plota os pontos originais (azul) e a linha de predição (vermelha).

⚠️ Erro no código: plt.plot(...) tem model.predict(X_train) perdido como terceiro argumento — isso vai dar erro. O correto seria:


 Aplicação prática:
Esse modelo representa regressão supervisionada, útil em situações como:

Previsão de preços (casas, ações, carros...).

Estimativa de produtividade com base em horas trabalhadas.

Qualquer problema onde exista uma relação linear entre entrada e saída.

💡 Resumo final:
Esse exemplo mostra o fluxo básico de um modelo de machine learning:

Definir dados.

Criar e compilar modelo.

Treinar (fit).

Prever e visualizar.

"""