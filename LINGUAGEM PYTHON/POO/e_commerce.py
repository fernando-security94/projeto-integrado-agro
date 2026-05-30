import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split



 

df = pd.read_csv('Train.csv')


fig, ax = plt.subplots(figsize=(8, 5))

sns.barplot(data=df, x='Reached.on.Time_Y.N', y='Discount_offered')
ax.set_title(f'Atraso na Entrega vc Desconto Oferecido', fontsize=16)
plt.show()

 

class DataPrep:

    def __init__(self, data):

        self.data = data

       

    @staticmethod

    def _one_hot_encoder(

            df: pd.DataFrame,

            variavel: str) -> pd.DataFrame:

            dummies = pd.get_dummies(df[variavel], prefix=variavel)

            df = pd.concat([df, dummies], axis=1)

            df.drop(columns=variavel, inplace=True)

            return df

           

    def _tratar_variaveis_categoricas(self) -> None:

            self.data = DataPrep._one_hot_encoder(

                self.data, 'Warehouse_block')

       

            self.data = DataPrep._one_hot_encoder(

                self.data, 'Mode_of_Shipment')

                

            self.data = DataPrep._one_hot_encoder(

                self.data, 'Product_importance')

                

            self.data = DataPrep._one_hot_encoder(

                self.data, 'Gender')

                

    def _remover_variaveis(self) -> None:

        self.data.drop(columns='ID', inplace=True)

       

    def _separar_treino_teste(self):

        treino, teste = train_test_split(

            self.data,

            test_size=0.3,

            random_state=2021)

        return treino, teste

       

    def preparar_dados(self):

        self._tratar_variaveis_categoricas()

        self._remover_variaveis()

        treino, teste = self._separar_treino_teste()

        return treino, teste   