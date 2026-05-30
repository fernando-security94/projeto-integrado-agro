'''Boa 👌. Esse seu script já modela bem um grafo direcionado de interações entre usuários.
A ideia central de identificar influenciadores é encontrar os nós 
com maior grau de entrada (muitos apontam para eles → recebem atenção/seguidores).

👉 Ajustes que fiz abaixo:

Corrigi o print que estava com sintaxe incompleta.

Deixei o código bem comentado.

Ajustei a lógica de identificar_influenciadores: 
em vez de só comparar com vizinhos diretos, ele pega os usuários com 
maior grau de entrada da rede (mais seguidos = mais influentes).
Acrescentei um método de centralidade de entrada para retornar os top influenciadores '''

class Grafo:
    def __init__(self):
        # Estrutura: {vertice: [lista_de_vizinhos]}
        self.adjacencias = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencias:
            self.adjacencias[vertice] = []

    def adicionar_aresta(self, vertice_origem, vertice_destino):
        """
        Adiciona uma aresta direcionada (origem -> destino),
        representando que 'origem' segue/interage com 'destino'.
        """
        self.adicionar_vertice(vertice_origem)
        self.adicionar_vertice(vertice_destino)
        self.adjacencias[vertice_origem].append(vertice_destino)

    def grau_entrada(self, vertice):
        """
        Retorna quantos seguidores/conexões de entrada o vértice possui.
        """
        grau = 0
        for vizinhos in self.adjacencias.values():
            if vertice in vizinhos:
                grau += 1
        return grau

    def identificar_influenciadores(self, top_n=3):
        """
        Identifica os principais influenciadores da rede:
        aqueles com maior grau de entrada.
        Retorna os 'top_n' usuários mais influentes.
        """
        graus = {usuario: self.grau_entrada(usuario) for usuario in self.adjacencias}
        # Ordena por grau de entrada (decrescente)
        influenciadores = sorted(graus.items(), key=lambda x: x[1], reverse=True)
        return influenciadores[:top_n]


# ==========================================
# Exemplo de uso do algoritmo
# ==========================================

rede_social = Grafo()

# Construindo a rede de interações (seguindo/seguido)
rede_social.adicionar_aresta('Alice', 'Bob')
rede_social.adicionar_aresta('Alice', 'Carol')
rede_social.adicionar_aresta('Bob', 'Alice')
rede_social.adicionar_aresta('Bob', 'Dave')
rede_social.adicionar_aresta('Carol', 'Alice')
rede_social.adicionar_aresta('Carol', 'Dave')
rede_social.adicionar_aresta('Dave', 'Bob')
rede_social.adicionar_aresta('Dave', 'Carol')
rede_social.adicionar_aresta('Dave', 'Eve')
rede_social.adicionar_aresta('Eve', 'Dave')

# Identificando influenciadores
influenciadores = rede_social.identificar_influenciadores(top_n=3)

print("Principais influenciadores da rede:")
for usuario, grau in influenciadores:
    print(f"- {usuario} (seguido por {grau} pessoas)")
