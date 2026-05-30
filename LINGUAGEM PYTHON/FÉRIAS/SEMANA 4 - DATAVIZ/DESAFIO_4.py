'''🔸 Desafio 4 – Visualização com Python e Tableau (Quinta)
🎯 Contexto:
Você tem dados de consumo de energia por mês e quer visualizar padrões.

🧠 Você vai treinar:
Criação de gráficos em Python

Construção de dashboards no Tableau (dados salvos em CSV)

💻 Desafio:
Crie um DataFrame com os meses e consumo (kWh)

Gere:

Gráfico de linha (evolução do consumo)

Gráfico de barras (comparação por mês)

Exporte o CSV para criar um dashboard no Tableau
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados
dados = {
    'mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'consumo_kwh': [250, 230, 270, 300, 280, 310]
}

df = pd.DataFrame(dados)

# Gráfico de linha
sns.lineplot(x='mes', y='consumo_kwh', data=df)
plt.title('Consumo de Energia (kWh)')
plt.show()
