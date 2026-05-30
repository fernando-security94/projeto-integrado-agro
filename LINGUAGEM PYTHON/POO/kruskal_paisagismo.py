class Grafo:
    def __init__(self, orientado=False):
        """
        Classe para representar grafos usando lista de adjacência.
        :param orientado: define se o grafo é orientado ou não.
        """
        self._lista_de_adjacencias = dict()
        self.orientado = orientado

    @property
    def vertices(self):
        """
        Retorna todos os vértices do grafo.
        """
        return set(self._lista_de_adjacencias.keys())

    def arestas(self, v_origem=None):
        """
        Retorna todas as arestas do grafo ou apenas as de um vértice específico.
        """
        if v_origem:
            return self.v_arestas(v_origem)

        arestas_do_grafo = []
        for v_origem in self.vertices:
            arestas_do_grafo += self.v_arestas(v_origem)
        return arestas_do_grafo

    def v_arestas(self, v_origem):
        """
        Retorna as arestas que saem de um vértice específico.
        """
        arestas = []
        for v_destino, custo in self._lista_de_adjacencias[v_origem]:
            arestas.append((v_origem, v_destino, custo))
        return arestas

    def inserir_aresta(self, u, v, custo):
        """
        Insere uma aresta entre dois vértices com o custo fornecido.
        Se o grafo não for orientado, adiciona em ambos os sentidos.
        """
        self._lista_de_adjacencias.setdefault(u, [])
        self._lista_de_adjacencias.setdefault(v, [])

        self._lista_de_adjacencias[u].append((v, custo))
        if not self.orientado:
            self._lista_de_adjacencias[v].append((u, custo))

    def inserir_arestas(self, arestas):
        """
        Insere várias arestas de uma vez.
        """
        for aresta in arestas:
            self.inserir_aresta(*aresta)

    def imprimir(self):
        """
        Imprime todas as arestas do grafo e o custo total.
        """
        total = 0
        for u, v, custo in self.arestas():
            print(f"{u} -- {v} (custo: {custo})")
            total += custo
        if not self.orientado:
            # dividir por 2 porque em grafos não orientados cada aresta aparece 2 vezes
            total = total / 2
        print(f"Custo total: {total}")


def kruskal(grafo):
    """
    Algoritmo de Kruskal para gerar a Árvore Geradora Mínima (MST).
    :param grafo: objeto da classe Grafo
    :return: grafo representando a MST
    """
    arestas_mst = set()

    # Conjunto disjunto inicial: cada vértice é seu próprio conjunto
    conjuntos = {v: {v} for v in grafo.vertices}

    # Ordena arestas pelo custo
    arestas_ordenadas = sorted(
        grafo.arestas(),
        key=lambda aresta: aresta[-1]
    )

    # Itera sobre arestas em ordem crescente
    for u, v, custo in arestas_ordenadas:
        if conjuntos[u].isdisjoint(conjuntos[v]):
            # Adiciona a aresta se não formar ciclo
            arestas_mst.add((u, v, custo))

            # União dos conjuntos de u e v
            uniao = conjuntos[u] | conjuntos[v]
            for vertice in uniao:
                conjuntos[vertice] = uniao

    mst = Grafo()
    mst.inserir_arestas(arestas_mst)
    return mst


# =========================
# TESTE DO ALGORITMO
# =========================
if __name__ == "__main__":
    print("=== TESTE AUTOMÁTICO (paisagismo fixo) ===")
    arestas = [
        ('Parquinho', 'Lago', 2.2),
        ('Quadras', 'Lago', 5.5),
        ('Parquinho', 'Quadras', 8.6),
        ('Lanchonete', 'Lago', 6),
    ]

    g1 = Grafo()
    g1.inserir_arestas(arestas)

    mst1 = kruskal(g1)
    mst1.imprimir()

    print("\n=== TESTE COM ENTRADA DO USUÁRIO ===")
    from itertools import combinations

    # Solicita locais
    qtd = int(input("Quantos locais o parque tem? "))
    locais = [input(f"Digite o nome do local {i+1}: ") for i in range(qtd)]

    # Solicita distâncias
    arestas_usuario = []
    for u, v in combinations(locais, 2):
        distancia = float(input(f"Digite a distância entre {u} e {v}: "))
        arestas_usuario.append((u, v, distancia))

    g2 = Grafo()
    g2.inserir_arestas(arestas_usuario)

    mst2 = kruskal(g2)
    mst2.imprimir()
