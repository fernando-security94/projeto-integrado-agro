# Exemplo de regressao multivariada com duas entradas:
# peso(kg) e altura(m) para prever o IMC

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import seaborn as sns
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import Input 


# Dados simulados: [peso (kg), altura (m)]
X_train = np.array([
    [60, 1.70],
    [72, 1.80],
    [85, 1.75],
    [90, 1.90],
    [120, 1.90],
    [90, 1.82],
    [94, 1.86],
    [80, 1.85]
], dtype=np.float32)

# Calculo da altura² e cria nova matriz com peso e altura²
altura_quadrado = X_train[:, 1] ** 2
X_train_corrigido = np.column_stack((X_train[:, 0], altura_quadrado))

# Calculo do IMC como alvo
Y_train = X_train[:, 0] / altura_quadrado 
Y_train = Y_train.reshape(-1, 1)

# Modelo de regressão multivariada
model = Sequential([
    Input(shape=(2,)),  # entrada = [peso, altura²]
    Dense(units=1)      # saída: IMC
])
model.compile(optimizer='adam', loss='mean_squared_error')

# Treinamento do modelo com .fit()
model.fit(X_train_corrigido, Y_train, epochs=2000, verbose=0)


# Previsão para novo indivíduo
# Exemplo: 70kg, 1.75m
novo_peso = 70
nova_altura = 1.75
nova_altura_quadrado = nova_altura ** 2
x_new_corrigido = np.array([[novo_peso, nova_altura_quadrado]], dtype=np.float32)

# Predição com os mesmos dados do treino
prediction = model.predict(X_train_corrigido)

print(f'Predição do IMC para 70kg e 1.75m de altura: {prediction[0][0]:.2f}')

# Visualizacao de dados com seaborn e pyplot
plt.figure(figsize=(8, 6))
sns.scatterplot(x=Y_train.flatten(), y=prediction.flatten(), color='royalblue', s=100, label='Predições')

# Linha de igualdade (idade = real)
plt.plot([Y_train.min(), Y_train.max()], [Y_train.min(), Y_train.max()], 'r--', label='Ideal')

plt.title('IMC Real vs IMC Previsto')
plt.xlabel('IMC Real (Cálculo Direto)')
plt.ylabel('IMC Previsto (Rede Neural)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()




"""
✅ O que você fez de certo:
Mais exemplos = mais aprendizado. Isso deu ao modelo mais contexto sobre o que é um IMC “normal”, evitando enviesamento com poucos dados.

Aumentou epochs = mais chances do modelo ajustar pesos corretamente, reduzindo o erro de predição.

Resultado 22.36 está bem próximo do valor real (22.86). Está ótimo para um modelo simples de regressão linear com dados artificiais!

🧠 Explicando o que está acontecendo:
O modelo está aprendendo a replicar a fórmula do IMC, mas como é uma rede neural e não uma equação explícita, ele aproxima com base nos padrões nos dados.

Como o formato de entrada foi alterado para [peso, altura²], o modelo consegue associar diretamente com o cálculo real.

🧠 Explicando o que está acontecendo:
O modelo está aprendendo a replicar a fórmula do IMC, mas como é uma rede neural e não uma equação explícita, ele aproxima com base nos padrões nos dados.

Como o formato de entrada foi alterado para [peso, altura²], o modelo consegue associar diretamente com o cálculo real.


"""

"""
Adicionar depois:
✅ 1. Erro Médio Absoluto (MAE)
Mede, em média, o quanto o modelo erra nas previsões (em unidades de IMC). Quanto menor, melhor.

✅ 2. Coeficiente de Determinação (R² Score)
Varia entre 0 e 1. Indica o quanto o modelo explica a variância dos dados. Quanto mais próximo de 1, melhor.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, r2_score

# Suponha que você já tenha Y_train e prediction prontos
# Se ainda não tiver, rode o modelo para gerar prediction

# Calcular métricas
mae = mean_absolute_error(Y_train, prediction)
r2 = r2_score(Y_train, prediction)

# Criar visualização
plt.figure(figsize=(8, 6))
sns.scatterplot(x=Y_train.flatten(), y=prediction.flatten(), color='royalblue', s=100, label='Predições')

# Linha ideal (Y = X)
plt.plot([Y_train.min(), Y_train.max()],
         [Y_train.min(), Y_train.max()],
         'r--', label='Ideal (Y = X)')

# Exibir métricas no gráfico
plt.text(Y_train.min(), Y_train.max() * 0.95,
         f'MAE: {mae:.2f}\nR²: {r2:.2f}',
         fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Títulos e legendas
plt.xlabel('IMC Real')
plt.ylabel('IMC Previsto')
plt.title('Desempenho da Regressão para Previsão de IMC')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""