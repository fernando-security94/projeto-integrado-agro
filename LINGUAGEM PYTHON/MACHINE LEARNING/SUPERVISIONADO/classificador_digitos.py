# Criação de um modelo que classifique os numerais
# que foram escritos a mão.
# vamos importar um dataset pronto

import tensorflow as tf

# dataset mnist pronto
'''O conjunto de dados MNIST é um conjunto de imagens de dígitos escritos à mão (0 a 9). 
É frequentemente usado como um ponto de partida para o aprendizado de máquina. 
x_train e x_test contêm as imagens, enquanto y_train e y_test contêm as etiquetas correspondentes.

As imagens são normalizadas dividindo-se cada pixel por 255.0. 
Isso coloca os valores dos pixels no intervalo [0, 1], facilitando o treinamento do modelo
'''


mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train, y_test = X_train / 255.0, X_test / 255.0


'''Cria-se, então, um modelo sequencial com as seguintes camadas:
Flatten: converte a matriz bidimensional das imagens (28x28 pixels) em um vetor unidimensional.

Dense(128, activation='relu'): camada densa com 128 neurônios e função de ativação ReLU.

Dropout(0.2): regularização por abandono, desativando aleatoriamente 20% dos neurônios 
durante o treinamento, para evitar overfitting.

Dense(10, activation='softmax'): camada de saída com 10 neurônios (um para cada dígito) 
e função de ativação softmax, que produzirá uma distribuição de probabilidade sobre as classes.'''

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# compilando o modelo
'''O modelo é compilado com o otimizador 'adam', 
a função de perda 'sparse_categorical_crossentropy' (adequada para problemas de classificação multiclasse) 
e a métrica de 'accuracy'.'''
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


# Treinando o modelos
'''O modelo é treinado usando-se o conjunto de treinamento (x_train e y_train) por cinco épocas.'''
model.fit(X_train, y_train, epochs=5)

'''O desempenho do modelo é avaliado utilizando-se o conjunto de teste (x_test e y_test), 
e os resultados, incluindo a perda e a precisão, são exibidos.'''
model.evaluate(X_test, y_test)


"""
O conjunto de dados MNIST é um conjunto de imagens de dígitos escritos à mão (0 a 9). 
É frequentemente usado como um ponto de partida para o aprendizado de máquina. 
x_train e x_test contêm as imagens, enquanto y_train e y_test contêm as etiquetas correspondentes.

As imagens são normalizadas dividindo-se cada pixel por 255.0. 
Isso coloca os valores dos pixels no intervalo [0, 1], facilitando o treinamento do modelo.

Cria-se, então, um modelo sequencial com as seguintes camadas:
Flatten: converte a matriz bidimensional das imagens (28x28 pixels) em um vetor unidimensional.

Dense(128, activation='relu'): camada densa com 128 neurônios e função de ativação ReLU.
Dropout(0.2): regularização por abandono, desativando aleatoriamente 20% dos neurônios 
durante o treinamento, para evitar overfitting.

Dense(10, activation='softmax'): camada de saída com 10 neurônios (um para cada dígito) 
e função de ativação softmax, que produzirá uma distribuição de probabilidade sobre as classes.

O modelo é compilado com o otimizador 'adam', 
a função de perda 'sparse_categorical_crossentropy' (adequada para problemas de classificação multiclasse) 
e a métrica de 'accuracy'.

O modelo é treinado usando-se o conjunto de treinamento (x_train e y_train) por cinco épocas.

O desempenho do modelo é avaliado utilizando-se o conjunto de teste (x_test e y_test), 
e os resultados, incluindo a perda e a precisão, são exibidos.

A arquitetura específica do modelo envolve uma camada inicial que “achata” as imagens bidimensionais 
em um vetor unidimensional, seguida por uma camada densa (totalmente conectada) com ativação ReLU, 
uma camada de dropout para regularização e, por fim, 
uma camada de saída com ativação softmax para gerar probabilidades a cada classe.

Após o treinamento, o modelo pode ser usado para prever a classe de um dígito desconhecido, 
e a avaliação no conjunto de teste fornece uma medida de quão bem ele generaliza para dados não vistos. 
A métrica de “accuracy” indica a proporção de previsões corretas em relação ao total de previsões.



"""