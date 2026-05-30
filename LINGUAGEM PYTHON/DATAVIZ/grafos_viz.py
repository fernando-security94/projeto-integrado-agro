# Importa as bibliotecas necessárias
import networkx as nx
import matplotlib.pyplot as plt


# Classe para visualização e manipulação de grafos
class VisualizacaoGrafo:

    # Inicializador da classe
    def __init__(self):
        # Lista que armazenará as arestas (ligações entre nós)
        self.visual = []

    # Método para adicionar uma aresta entre dois vértices (nós)
    def adicionaAresta(self, a, b):
        """
        Adiciona uma ligação (aresta) entre os nós 'a' e 'b'.
        """
        temp = [a, b]
        self.visual.append(temp)

    # Método para desenhar o grafo com o NetworkX
    def desenhar(self):
        """
        Cria o grafo com as arestas adicionadas e exibe sua visualização.
        """
        G = nx.Graph()  # Cria o objeto grafo
        G.add_edges_from(self.visual)  # Adiciona todas as arestas
        # Desenha o grafo: nós em cinza claro, bordas em preto
        nx.draw_networkx(G, node_color='lightgrey', edge_color='black')
        plt.show()


# -------------------- TESTES --------------------

# Cria uma instância da classe
grafo = VisualizacaoGrafo()

# Adiciona arestas representando relações
grafo.adicionaAresta('Pedro', 'CP')
grafo.adicionaAresta('Pedro', 'Carla')
grafo.adicionaAresta('Carla', 'CP')
grafo.adicionaAresta('Pedro', 'CC')
grafo.adicionaAresta('Joao', 'CC')

# Teste 1: verificar se as arestas foram adicionadas
print("Arestas armazenadas:", grafo.visual)

# Teste 2: verificar se o número de arestas está correto
assert len(grafo.visual) == 5, "Erro: número de arestas diferente do esperado!"

# Teste 3: verificar se uma aresta específica existe
assert ['Pedro', 'Carla'] in grafo.visual or ['Carla', 'Pedro'] in grafo.visual, \
    "Erro: a aresta Pedro-Carla não foi adicionada corretamente!"

print("Todos os testes passaram com sucesso!")

# Exibe o grafo
grafo.desenhar()


'''
Nesse exemplo, a classe visualizacaoGrafo é utilizada para construir um grafo 
que ilustra as relações entre pessoas (Pedro, Carla, João) e suas contas 
(CP - Conta Poupança, CC - Conta Corrente). 
A lista visual armazena as arestas do grafo, onde cada aresta é 
uma relação entre dois vértices (por exemplo, uma pessoa e uma conta ou 
relações entre pessoas).

Após adicionar as arestas desejadas utilizando o método adicionaAresta, 
o método desenhar cria uma instância de um grafo com a biblioteca NetworkX, 
adiciona as arestas a partir da lista visual e, finalmente, desenha o grafo na 
tela utilizando a função draw_networkx da NetworkX, com a cor dos nós definida 
como cinza claro para melhor visualização.

Esse script é um exemplo prático de como representar e visualizar relações complexas 
de forma intuitiva e visual com grafos em Python.

A Figura 3 exibe o grafo gerado a partir das arestas definidas anteriormente. 
O layout dos vértices e das arestas varia automaticamente pelo software para 
prevenir sobreposições e garantir uma visualização clara. Calcular esses posicionamentos 
é uma tarefa complexa que requer expertise em computação gráfica, justificando 
o uso de bibliotecas como a NetworkX. Notavelmente, na construção do grafo, 
não especificamos parâmetros de posicionamento, evidenciando a capacidade da biblioteca 
de organizar os elementos do grafo de forma autônoma.

'''