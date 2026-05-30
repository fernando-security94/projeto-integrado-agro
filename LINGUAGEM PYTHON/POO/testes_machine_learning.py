# Utilizando dataset titanic do seaborn

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve, RocCurveDisplay

# Carregando dataset
df = sns.load_dataset('titanic')
print('Exibição de todas as colunas:')
print(df.columns)
print()


class DataPrep:
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data.copy()

    def remover_variaveis(self) -> None:
        colunas_para_remover = [
        'passenger_id', 'name', 'ticket', 'cabin',  # já estava
        'class', 'who', 'deck', 'embark_town', 'alive', 'adult_male'  # novas colunas do tipo object/bool
    ]
        self.data.drop(columns=colunas_para_remover, inplace=True, errors='ignore')


    def tratar_nulos(self) -> None:
        # Corrigido: preenche 'age' com mediana do grupo com transform (índices preservados)
            self.data['age'] = self.data['age'].fillna(
            self.data.groupby(['pclass', 'sex'])['age'].transform('median')
        )

        # Preenchimento padrão para embarque ausente
            self.data['embarked'] = self.data['embarked'].fillna('S')


    def tratar_variaveis_categoricas(self) -> None:
        sexo = {'male': 0, 'female': 1}
        self.data['sex'] = self.data['sex'].map(sexo)

        embarked_dummies = pd.get_dummies(self.data['embarked'], prefix='embarked')
        self.data = pd.concat([self.data, embarked_dummies], axis=1)
        self.data.drop(columns=['embarked'], inplace=True)

    def normalizar_dados(self) -> None:
        print("Tipos das colunas antes da normalização:")
        print(self.data.dtypes)

        resposta = self.data['survived'].reset_index(drop=True)
        variaveis = self.data.drop(columns='survived').reset_index(drop=True)

        scaler = MinMaxScaler()
        variaveis_normalizadas = scaler.fit_transform(variaveis)
        variaveis_df = pd.DataFrame(variaveis_normalizadas, columns=variaveis.columns)

        self.data = pd.concat([variaveis_df, resposta], axis=1)

    def separar_treino_teste(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        return train_test_split(self.data, test_size=0.3, random_state=2021)

    def preparar_dados(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        self.tratar_nulos()
        self.tratar_variaveis_categoricas()
        self.remover_variaveis()
        self.normalizar_dados()
        return self.separar_treino_teste()


# Preparação dos dados
prep = DataPrep(df)
treino, teste = prep.preparar_dados()

X_treino = treino.drop(columns='survived')
y_treino = treino['survived']

X_teste = teste.drop(columns='survived')
y_teste = teste['survived']

# Treinamento e avaliação do modelo
clf = LogisticRegression(max_iter=1000)
clf.fit(X_treino, y_treino)
y_pred = clf.predict(X_teste)



# Curva ROC

# Obtendo as probabilidades da classe positiva (sobreviveu = 1)
y_proba = clf.predict_proba(X_teste)[:, 1]

# Calculando as taxas FPR (false positive rate) e TPR (true positive rate)
fpr, tpr, thresholds = roc_curve(y_teste, y_proba)

# Exibindo a curva ROC
roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr)
roc_display.plot()
plt.show()






print("Score de acurácia:", accuracy_score(y_teste, y_pred))
print()

# Estatísticas adicionais
print("Exibição de total de valores null:")
print(df.isna().sum())
print()

print("Exibição de mediana das idades:")
print(df['age'].median())
print()

print('Exibindo relação média com classe e sexo:')
print(df.groupby(['pclass', 'sex'], as_index=False)['age'].median())
print()






'''
✅ Principais Ajustes Feitos
Corrigida a aplicação de groupby().apply() para imputar idades.

Corrigida a criação de DataFrame após normalização.

Corrigido uso de get_dummies para colunas categóricas.

Corrigido o fluxo de separação treino/teste.

Corrigido uso do modelo LogisticRegression.

Corrigido print de resultados de forma clara.



'''








# import seaborn as sns
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score


# df = sns.load_dataset('titanic')
# # print(df.head())
# print('Exibição de todas as colunas:')
# print(df.columns)
# print()


# class DataPrep:
#     def __init__(self, data: pd.DataFrame)-> None:
#         self.data = data

#     def remover_variaveis(self) -> None:
#         colunas_para_remover = [
#             'passenger_id',
#             'name',
#             'ticket',
#             'cabin',
#             'embarked'
#         ]
#         self.data.drop(columns=colunas_para_remover, inplace=True)

#     def tratar_nulos(self)-> None:
#         self.data['age'] = self.data.groupby(['pclass', 'sex'])
#         ['age'].apply(lambda x : x.fillna(x.median())).reset_index(drop=True)
#         self.data['embarked'] = self.data['embarked'].fillna('S')

#     def tratar_variaveis_categoricas(self) -> None:
#         sexo = {'male': 0, 'female': 1}
#         self.data['sex'] = self.data['sex'].map(sexo)

#         embarked_dummies = pd.get_dummies(self.data['embarked'])
#         self.data = pd.concat([self.data, embarked_dummies], axis=1)

#     def normalizar_dados(self)-> None:
#         variaveis = self.data.drop(columns='survived')
#         var_cols = variaveis.columns
#         resposta = self.data['survived']

#         scaler = MinMaxScaler()
#         variaveis = scaler.fit_transform(variaveis)
#         variaveis - pd.DataFrame(variaveis, columns=var_cols)

#         self.data = pd.concat([variaveis, resposta], axis=1)

#     def separar_treino_teste(self)-> tuple[pd.DataFrame, pd.DataFrame]:
#         treino, teste = train_test_split(self.data, test_size=0.3, random_state=2021)
#         return treino, teste
    
#     def preparar_dados(self)-> tuple[pd.DataFrame, pd.DataFrame]:
#         self.tratar_nulos()
#         self.tratar_variaveis_categoricas()
#         self.remover_variaveis()
#         self.normalizar_dados()
#         treino, teste = self.separar_treino_teste()
#         return treino, teste
    
# # Variaveis de treino e teste
# df_treino= DataPrep(df)
# df_teste= DataPrep(df)
# df_treino.preparar_dados()
# X_treino = df_treino.drop(columns='survived')
# y_treino = df_treino['survived']


# X_teste = df_teste.drop(columns='survived')
# y_teste = df_teste['survived']

# clf = LogisticRegression()
# clf.score = (X_teste, y_teste)

# print("Score de acurácia: ")
# accuracy_score(X_teste, y_teste)
    


# print("Exibição de total de valores null:")
# print(df.isna().sum())
# print()

# print("Exibição de mediana das idades:")
# print(df['age'].median())
# print()

# print('Exibindo relação média com classe e sexo:')
# print(df.groupby(['pclass', 'sex'], as_index=False)['age'].median())
# print()