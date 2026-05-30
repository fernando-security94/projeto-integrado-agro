# Modelagem de regressão logística

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from testes_machine_learning import DataPrep

df = sns.load_dataset('titanic')
print(df.columns)
print(df.head())

# Modelo de Estimador
# estimator = LinearRegression()
# estimator.fit(X_train, Y_train)
# y_pred = estimator.predict(X_test)

print(df.isna().sum())

# Remover linhas com valores ausentes em 'fare' ou 'survived'
df = df[['fare', 'survived']].dropna()


# Modelo de  Transformador
# transformer = StandardScaler()
# X_train_scaled = transformer.fit_transform(X_train)
# X_test_scaled = transformer.transform(X_test)


# Modelo de Previsão
# predictor = RandomForestClassifier()
# predictor.fit(X_train, y_train)
# y_pred = predictor.predict(X_test)





X = df['fare'].copy()
X = X.values.reshape(-1, 1)
y = df['survived'].copy()


# treinamento do modelo para regressão logística
regressao_logistica = LogisticRegression()
regressao_logistica.fit(X, y)
print(f'\nScore da regressão logística: {regressao_logistica.score(X, y)}\n')

# dp = DataPrep(df)
# df_treino, df_teste = dp.preparar_dados()

# X_treino = df_treino.drop(columns='survived')
# y_treino = df_treino['survided']

# X_teste = df_teste.drop(columns='survived')
# y_teste = df_teste['survided']

# regressao_logistica.fit(X_treino, y_teste)
# regressao_logistica.score(X_teste, y_teste)


# Criar uma faixa de valores para 'fare'
fare_range = np.linspace(X.min(), X.max(), 300).reshape((-1, 1))  # matriz 2D

# obter probabilidades previstas de sobrevivencia
probabilidades = regressao_logistica.predict_proba(fare_range)[:, 1]  # probabilidade de sobreviver, classe 1



# após o treinamento do modelo, podemos realizar predições
# Quanto mais proximo de 1, maiores as chances


print("Predição de regressão logística para fare = 50")
print(regressao_logistica.predict_proba(np.array([[50]])))
print()
# Predições para passageiros que compraram passagem com fare = 50
# Result = 054524685 (Chance de morrer) / 0.45475315 (chance de não morrer)

print("\nPredição de regressão logística para fare = 70")
print(regressao_logistica.predict_proba(np.array([[70]])))

# Predições para passageiros que compraram passagem com fare = 70
# Result = 0.46942832 (chance de morrer) / 0.53057168 (chance de nao morrer)


# Plotagem da curva
plt.figure(figsize=(10, 6))
plt.plot(fare_range, probabilidades, color='blue')
plt.title('Curva de Decisão - Regressão Logística (Fare x Sobrevivência)')
plt.xlabel('Fare (Valor da Tarifa)')
plt.ylabel('Probabilidade de Sobrevivência')
plt.grid(True)
plt.tight_layout()
plt.show()