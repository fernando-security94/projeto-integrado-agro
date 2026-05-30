# Importando as bibliotecas necessárias
import matplotlib.pyplot as plt
import networkx as nx

# =============================
# Exemplo prático: Grafo de transações com cartão de crédito
# Cada aresta representa uma relação de transação entre cliente e loja
# =============================

# Definindo as arestas do grafo
# Cada tupla representa uma transação (Cliente <-> Loja ou Cliente <-> Cliente)
edges = [
    ('Loja 1', 'Cliente 1'),
    ('Cliente 1', 'Cliente 2'),
    ('Cliente 2', 'Loja 3')   # corrigido: antes estava 'Cliente' sem número
]

# Criando um grafo não direcionado
G = nx.Graph()

# Adicionando as conexões (arestas) ao grafo
G.add_edges_from(edges)

# =============================
# Layout do grafo
# O spring_layout organiza os nós de forma a reduzir sobreposição
# =============================
pos = nx.spring_layout(G, seed=42)  # seed para manter consistência no layout

# =============================
# Configuração da visualização
# =============================
plt.figure(figsize=(8, 6))  # tamanho da figura

# Desenhando o grafo com estilo customizado
nx.draw(
    G, pos,
    edge_color='black',
    width=1,
    linewidths=1,
    node_size=1000,
    node_color='lightblue',
    alpha=0.9
)

# Adicionando rótulos nos nós
labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_color='black')

# =============================
# Rótulos nas arestas (simulação de número de transações)
# =============================
edge_labels = {
    ('Loja 1', 'Cliente 1'): 'Transações: 2',
    ('Cliente 1', 'Cliente 2'): 'Transações: 5',
    ('Cliente 2', 'Loja 3'): 'Transações: 7'
}

# Exibindo os rótulos das arestas em vermelho
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# =============================
# Finalizando o gráfico
# =============================
plt.title("Rede de Transações com Cartão de Crédito", fontsize=14)
plt.axis('off')  # remove eixos
plt.show()



# Modelo com transações agregadas em uma unica aresta com peso
# Única conexão com peso acumulado

import networkx as nx
import matplotlib.pyplot as plt

# ==============================
# Grafo bipartido Cliente–Loja
# ==============================

# Criando o grafo bipartido
G = nx.Graph()

# Conjuntos de nós
clientes = ["Cliente"]
lojas = ["Loja 1", "Loja 2", "Loja 3"]

# Adicionando nós com atributo de bipartição
G.add_nodes_from(clientes, bipartite=0)  # lado 0
G.add_nodes_from(lojas, bipartite=1)     # lado 1

# Transações simuladas (Cliente, Loja, Número de transações)
transacoes = [
    ("Cliente", "Loja 1", 5),
    ("Cliente", "Loja 2", 3),
    ("Cliente", "Loja 3", 7)
]

# Adicionando arestas com peso (número total de transações)
for cliente, loja, qtd in transacoes:
    G.add_edge(cliente, loja, weight=qtd)

# ==============================
# Visualização do grafo
# ==============================
pos = nx.spring_layout(G, seed=42)  # layout para posicionar os nós

plt.figure(figsize=(6, 6))
nx.draw(
    G, pos,
    with_labels=True,
    node_size=2000,
    node_color="lightgray",
    font_size=10,
    font_weight="bold"
)

# Desenhando os pesos das arestas
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color="red")

plt.title("Grafo Cliente–Loja com Pesos (Transações)", fontsize=12)
plt.show()
