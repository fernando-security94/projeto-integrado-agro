'''Você foi contratado para criar um modelo de Machine Learning 
que classifica espécies de flores Iris com base em características 
como comprimento e largura das sépalas e pétalas. 
Você usará o TensorFlow para construir, treinar e avaliar o modelo.'''

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf # biblioteca para construir e treinar o modelo de ML
import pandas as pd  # Usada para manipulação de dados
from sklearn.datasets import load_iris  # Dataset pronto do scikit-learn
from sklearn.model_selection import train_test_split  # Para dividir os dados em treino e teste
from sklearn.preprocessing import StandardScaler  # Para padronizar os dados


# carregar dataset iris

iris = load_iris()  
X = iris.data  # características como comprimento/largura, sépala e pétala
y = iris.target  # Aqui são os rótulos (0= setosa, 1= versicolor, 2= virginica)


# Fase de pré-processamento dos dados
#Essa função divide os dados em 80% para treino e 20% para teste, 
# garantindo que o modelo seja avaliado com dados que nunca viu.
X_train, X_test, y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados com StandardScaler()

scaler = StandardScaler()  # Criando um padronizador de média = 0 e desvio padrão = 1
X_train = scaler.fit_transform(X_train)  # Ajusta o scaler nos dados de treino
X_test = scaler.transform(X_test)  # Mesmo scaler para transformar os dados de teste


# Construção do modelo de Rede Neural
# Tendo a primeira camada com 10 neurônios
# Função Sequential significa que o modelo tem camadas em sequência
# Dense mantém as camadas totalmente conectadas
# activation='relu' auxilia a rede a aprender padrões não-lineares
# softmax = transforma a saída em probabilidades, um para cada classe.
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(10, activation='relu'),  # segunda camada oculta
    # camada de saída: 3 neurônios, 1 para cada classe
    tf.keras.layers.Dense(3, activation='softmax')  
    
])

# Compilação do Modelo
# optimizer='adam' é um otimizador moderno e eficiente
# loss='sparse_categorical_crossentropy - Função de perda para classificação com rótulos
# metrics=['accuracy'] - É a métrica da avaliação

# O compilador define como o modelo será treinado: 
# como medir o erro (loss), como atualizar os 
# pesos (optimizer), e como avaliar o 
# desempenho (accuracy).
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


# Treinamento do modelo
# O modelo vai percorrer os dados por 100x
# a cada passagem, a idéia é reduzir a margem de erros.
model.fit(X_train, y_train, epochs=100, verbose=1)


# Avaliar o modelo
# Aqui você mede o desempenho do modelo com os dados de teste. 
# O ideal é que ele acerte bem 
# mesmo com dados que nunca viu.
loss, accuracy = model.evaluate(X_test, Y_test)
print(f'Acurácia: {accuracy:.2f}')

# Gera probabilidades para cada classe
predictions = model.predict(X_test)

# Valores de previsão e valor real do primeiro item do teste.
# predict() retorna as probabilidades para cada classe. 
# argmax() pega a classe com maior valor.
print("Probabilidades:", predictions[0])
print("Classe prevista: ", np.argmax(predictions[0]))
print("Classe real: ", Y_test[0])

# Aqui vamos transformar o dataset em DataFrame para dataviz
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)



# Dataviz que retrata a distribuição por especie
# pairplot() exibe a características se relacionam entre si
# adicionando por espécie.
sns.pairplot(df, hue='species', diag_kind='hist')
plt.suptitle('Distribuição das Características por especie', y=1.02)
plt.show()


# Boxplot exibe a separação entre as classes
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='species', y='petal length (cm)')
plt.title('Comprimento da Pétala por Espécie')
plt.show()


# Matriz de correlação
# Isso mostra quais variáveis estão mais relacionadas 
# (útil para saber se há redundância ou forte ligação entre elas).

'''
Explicação do que está sendo feito:
df.drop(columns=['target', 'species']): remove colunas que não são numéricas.

.corr(): calcula a correlação entre as colunas numéricas restantes.

sns.heatmap(...): cria o mapa de calor para visualizar essas correlações.
'''


plt.figure(figsize=(8,6))
sns.heatmap(df.drop(columns=['target', 'species']).corr(), annot=True, cmap='coolwarm')
plt.title('Correlação entre as características')
plt.show

'''
Excelente! Vamos seguir com o projeto e adicionar visualizações do desempenho 
do modelo durante o treinamento, além de comparar previsões vs. rótulos reais. 
Tudo isso te ajuda a "enxergar" o aprendizado do modelo — entender se ele está melhorando, 
se está errando muito, onde erra, etc.
'''

# Vamos visualizar a acurácia e o loss durante o treinamento.
# Comparar previsões vs classes reais com gráfico como matriz de confusão
# Interpretar esses gráficos pra avaliar se o modelo está aprendendo bem.

# Capturar o histórico do treinamento
'''
O model.fit() retorna um objeto History com os dados de treino em cada época: 
loss e accuracy. 
'''
history = model.fit(X_train, y_train, epochs=100, verbose=1)

# Vamos plotar a acurácia e perda ao longo das epochs

# Accuracy
plt.figure(figsize=(10,4))
plt.plot(history.history['accuracy'], label='Acurácia (treino)')
plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.title('Evolução da Acurácia durante o Treinamento')
plt.legend()
plt.grid(True)
plt.show()


# Loss
plt.figure(figsize=(10,4))
plt.plot(history.history['loss'], label='Perda (treino)', color='red')
plt.xlabel('Época')
plt.ylabel('Perda (Loss)')
plt.title('Evolução da Perda durante o Treinamento')
plt.legend()
plt.grid(True)
plt.show()

'''
Esses gráficos mostram se o modelo 
está melhorando ou piorando com o tempo.
Se a acurácia sobe e a perda cai, está indo bem.
Se acurácia estagna ou cai, pode estar overfitting (memorizando em vez de generalizar).

'''

# Criação de Matriz de Confusão que:
'''
A matriz de confusão mostra quantas flores 
de cada espécie o modelo classificou certo ou errou.

'''

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Prever classes
y_pred = model.predict(X_test)
ypred_classes = tf.argmax(y_pred, axis=1).numpy()


# Criar matriz
cm = confusion_matrix(Y_test, ypred_classes)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)


# Exibição
'''
A diagonal mostra os acertos (ex: Setosa prevista como Setosa).
Os valores fora da diagonal são erros 
(ex: Virginica classificada como Versicolor).

'''

disp.plot(cmap='Blues')
plt.title('Matriz de Confusão')
plt.grid(False)
plt.show()


# classificação de previsões vs reais em um
# DataFrame

results = pd.DataFrame({
    'Real': pd.Categorical.from_codes(Y_test, iris.target_names),
    'Previsto': pd.Categorical.from_codes(ypred_classes, iris.target_names)

})

print(results.head(10))  # Exibe os 10 primeiros casos

