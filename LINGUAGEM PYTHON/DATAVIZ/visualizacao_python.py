# exemplo de dataviz com python
import matplotlib.pyplot as plt
import random

dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)

plt.figure(figsize=(10, 6))
plt.bar(dados1, dados2, color='royalblue', width=0.8)
plt.xlabel('Dados_1')
plt.ylabel('Dados_2')
plt.title('Grafico com valores random')
plt.show()











'''
import matplotlib.pyplot as plt
import random

dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)

plt.figure(figsize=(12, 6))  # ajusta o tamanho da figura ANTES do gráfico

plt.bar(dados1, dados2, color='skyblue')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico com Tamanho Personalizado')
plt.tight_layout()  # opcional, melhora o espaçamento automático
plt.show()


'''







'''
import pandas as pd

dados = {
    'Produto': ['A', 'B', 'C'],
    'Qtde_vendida': [33, 50, 45]
}

df = pd.DataFrame(dados)
df.plot(x='Produto', y='Qtde_vendida', kind='bar', color='royalblue')
df.plot(x='Produto', y='Qtde_vendida', kind='pie')
df.plot(x='Produto', y='Qtde_vendida', kind='line', color='royalblue')

print(df.head())



'''
