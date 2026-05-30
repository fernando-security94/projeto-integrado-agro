import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# criando DataFrame
dados = {
    'Nome': ['Ana', 'Bruno','Carlos','Diana'],
    'Idade': [23, 35, 31, 19],
    'Nota': [8.5, 7.0, 9.2, 6.8]
}

df = pd.DataFrame(dados)
print(df)
print()

# adicionar coluna de "aprovado" no dataFrame
df['Aprovado'] = df['Nota'] >= 7
aprovados = df[df['Aprovado']]
print("Alunos aprovados:")
print(aprovados)
print()


# exibir apenas pessoas com notas maior que 7
nota_maior_sete = df[df['Nota'] > 7.0]  
print('Pessoas com notas maior que 7:')
print(nota_maior_sete)
print()


# exibir apenas os nomes com nota maior que 7
nomes = df[df['Nota'] > 7.0]['Nome']  # adicionar a coluna que eu desejo exibir
print('Nomes das pessoas com notas maior que 7:')
print(nomes)

'''
🔵 Resumindo:

df['Nota'] > 7.0 faz o filtro (cria um filtro booleano).

Depois aplicamos isso no df[...].

Se quiser uma coluna específica, ainda usa ['Nome'] no final.
'''

# criar um grafico em matplotlib com as notas
plt.bar(df['Nome'], df['Nota'], color='royalblue')
plt.title('Nota dos alunos')
plt.xlabel('Nome')
plt.ylabel('Nota')
plt.show()

# criando grafico em seaborn
sns.scatterplot(x='Idade', y='Nota', data=df)
plt.grid(True)
plt.show()  # serve para pyplot e seaborn


# grafico de barras colorido no seaborn
sns.barplot(x='Nome', y='Nota', data=df, palette='pastel')  # 'deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind'
plt.title('Nota dos alunos')
plt.xlabel('Nome')
plt.ylabel('Nota')
plt.show()


# scatterplot com etiquetas
plt.figure(figsize=(8,6))
sns.scatterplot(x='Idade', y='Nota', data=df)

# adiciona os nomes dos alunos nos pontos
for i in range(df.shape[0]):  # numero de alunos por linhas
    plt.text(df['Idade'][i] + 0.5, df['Nota'][i], df['Nome'][i])  ## add texto no grafico

plt.grid(True)
plt.title('Notas x Idades')
plt.show()


# salvar em HTML
df.to_html('alunos.html', index=False)
print('Arquivo HTML "alunos.html" savlo com sucesso')