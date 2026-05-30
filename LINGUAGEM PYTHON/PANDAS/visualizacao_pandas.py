# exemplo de visualizacao de dados com pandas

import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Produto': ['A', 'B', 'C'],
    'qtde_vendida': [33, 50, 45]
}

df = pd.DataFrame(dados)
df.plot(x='Produto', y='qtde_vendida', kind='bar', color='royalblue')
df.plot(x='Produto', y='qtde_vendida', kind='pie')
df.plot(x='Produto', y='qtde_vendida', kind='line')

# exibir grafico
plt.show()

