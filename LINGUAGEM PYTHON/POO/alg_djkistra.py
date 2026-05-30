# Algoritmo de Dijkstra aplicado a um problema de logística
# Objetivo: encontrar o caminho de menor custo entre os pontos de entrega

# Grafo representado como dicionário de adjacência
# As chaves são os pontos (nós), e os valores são os vizinhos com seus respectivos custos
grafo = {
    'D': {'A': 2, 'B': 4},
    'A': {'D': 2, 'C': 1, 'B': 3},
    'B': {'A': 3, 'D': 4, 'E': 2},
    'C': {'A': 1, 'F': 4},
    'E': {'B': 2, 'F': 3},
    'F': {'C': 4, 'E': 3}
}

def dijkstra(grafo, inicio):
    # Distâncias mínimas conhecidas até cada nó
    menor_distancia = {vertice: float('inf') for vertice in grafo}
    menor_distancia[inicio] = 0  # Distância do ponto inicial é zero
    
    # Antecessores: para reconstruir o caminho ótimo
    antecessor = {}

    # Conjunto de nós a visitar
    nao_visitados = set(grafo.keys())

    while nao_visitados:
        # Escolher o vértice com a menor distância conhecida
        vertice_minimo = min(
            nao_visitados, key=lambda vertice: menor_distancia[vertice]
        )
        
        nao_visitados.remove(vertice_minimo)

        # Atualizar distâncias dos vizinhos
        for vizinho, peso in grafo[vertice_minimo].items():
            if menor_distancia[vertice_minimo] + peso < menor_distancia[vizinho]:
                menor_distancia[vizinho] = menor_distancia[vertice_minimo] + peso
                antecessor[vizinho] = vertice_minimo

    return menor_distancia, antecessor

def reconstruir_caminho(antecessor, inicio, fim):
    """Reconstrói o caminho ótimo do início ao destino."""
    caminho = []
    atual = fim
    while atual != inicio:
        caminho.insert(0, atual)
        atual = antecessor.get(atual)
        if atual is None:
            return None  # Não há caminho possível
    caminho.insert(0, inicio)
    return caminho

# === Exemplo de uso ===
inicio = 'D'
fim = 'F'

distancias, antecessores = dijkstra(grafo, inicio)
caminho_otimo = reconstruir_caminho(antecessores, inicio, fim)

print(f"📦 Melhor rota de {inicio} até {fim}: {caminho_otimo}")
print(f"💰 Custo total: {distancias[fim]}")
print(f"🗺️ Distâncias mínimas a partir de {inicio}: {distancias}")


'''
Inicialização: Define-se a matriz de adjacência do grafo e 
inicializa-se o algoritmo com distâncias infinitas para todos os vértices, 
exceto o ponto de partida (D), que recebe distância 0.

Processamento: O algoritmo itera sobre os vértices não visitados, 
selecionando o vértice com a menor distância acumulada em cada passo. 
Atualiza-se a menor distância para os vértices adjacentes, baseando-se nas
distâncias dos vértices já processados.

Resultado: O algoritmo retorna a menor distância de D para todos os 
outros vértices e o caminho a partir do depósito, permitindo à empresa de logística 
otimizar suas rotas de entrega.


'''