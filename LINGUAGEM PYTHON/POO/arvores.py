class Vertice:
    """
    Classe que representa um vértice (nó) de uma Árvore Binária.
    Cada vértice contem:
    - Um dado (conteudo armazenado)
    - Um ponteiro para o filho da esquerda
    - Um ponteiro para o filho da direita
    """
    def __init__(self, dado):
        """
        Inicializa um vértice da arvore binária
        :paramet dado: Conteúdo armazenado no vertice
        """
        self.dado = dado
        self.esquerda = None  # Filho à esquerda
        self.direita = None  # Filho à direita

    def __str__(self):
        # Retorna o valor do vértice como str (para facilitar impressao)
        return str(self.dado)
    

    # Métodos de representação
    def representa_parenteses(self):
        """
        Retorna uma representação textual da arvore usando parenteses
        de forma recursiva
        Exemplo: (A (B () ()) C () ())
        """
        # Representação do filho esquerdo
        left = self.esquerda.representa_parenteses() if self.esquerda else ""
        # representação do filho esquerdo
        right = self.direita.representa_parenteses() if self.direita else ""
        # Monta a string: (valor esquerdo direito)
        return "({} {} {})".format(str(self), left, right)
    
    def representa_recuo(self, numero_espacos = 0):
        """
        Retorna uma apresentação de arvore com recuo, onde cada nivel é
        identado por espaços para facilitar a visualização hierárquica
        """

        # Representação do filho esquerdo (com recuo maior)
        left = self.esquerda.representa_recuo(numero_espacos + 4) if self.esquerda else ""
        # Representação do filho direito (com recuo menor)
        right = self.direita.representa_recuo(numero_espacos + 4) if self.direita else ""
        # Monta a string formatada
        return "{espacos}{self}\n{left}{right}".format(espacos= " " * numero_espacos, self=str(self), left=left, right=right)
    

    # Métodos de percurso (Transversal)

    def imprimir_ordem(self):
        """
        Percorre a arvore em ordem simetrica (Esquerda -> Raiz -> Direita)
        e imprime o dado de cada vértice
        """
        if self.esquerda:
            self.esquerda.imprimir_ordem()  # visita esquerda
        print(self)  # visita raiz
        if self.direita:
            self.direita.imprimir_ordem()  # visita a direita

    def imprimir_pre_ordem(self):
        """
        Percorre a arvore em pré-ordem (Raiz -> Esquerda -> Direita)
        e imprime o dado de cada vértice
        """
        print(self)  # Visita raiz
        if self.esquerda:
            self.esquerda.imprimir_pre_ordem()  # visita esquerda
        if self.direita:
            self.direita.imprimir_pre_ordem()  # visita direita

    
    def imprimir_pos_ordem(self):
        """
        Percorre a árvore em pós-ordem (Esquerda -> Direita -> Raiz)
        e imprime o valor de cada vertice
        """
        if self.esquerda:
            self.esquerda.imprimir_pos_ordem()  # visita esquerda
        if self.direita:
            self.direita.imprimir_pos_ordem()  # visita direita
        print(self)  # Vistia raiz


# Criação da representação gráfica da arvore
from graphviz import Digraph

# -------- Função utilitária para desenhar a árvore com Graphviz --------
def desenhar_arvore(raiz, nome_arquivo="arvore_binaria", formato="png"):
    """
    Gera uma imagem (png/pdf/svg etc.) da árvore binária usando Graphviz.

    Passo a passo:
    1) Cria um grafo direcionado (Digraph) e define estilo/layout.
    2) Percorre recursivamente a árvore:
       - Adiciona cada nó com um ID único (usaremos id(no)) e rótulo = no.dado.
       - Cria arestas do nó pai para os filhos esquerdo (E) e direito (D).
    3) Renderiza o arquivo no formato desejado e retorna o caminho gerado.

    :param raiz: (Vertice) nó raiz da árvore
    :param nome_arquivo: (str) nome base do arquivo de saída (sem extensão)
    :param formato: (str) 'png', 'pdf', 'svg', etc.
    :return: (str) caminho do arquivo gerado (ex.: 'arvore_binaria.png')
    """
    dot = Digraph(comment="Árvore Binária")
    dot.attr(rankdir="TB")                 # Top-to-Bottom (raiz em cima)
    dot.attr("node", shape="circle")       # Nós circulares (estético)

    def adicionar(no):
        if not no:
            return
        # Cria o nó no gráfico:
        # - ID interno: str(id(no)) garante unicidade
        # - label: o dado do vértice (o que aparece desenhado)
        dot.node(str(id(no)), label=str(no.dado))

        # Se houver filho à esquerda, cria aresta Pai -> Esquerda
        if no.esquerda:
            dot.edge(str(id(no)), str(id(no.esquerda)), label="E")  # E = Esquerda (opcional)
            adicionar(no.esquerda)

        # Se houver filho à direita, cria aresta Pai -> Direita
        if no.direita:
            dot.edge(str(id(no)), str(id(no.direita)), label="D")   # D = Direita (opcional)
            adicionar(no.direita)

    adicionar(raiz)

    # Gera o arquivo (ex.: arvore_binaria.png) e retorna o caminho
    caminho = dot.render(filename=nome_arquivo, format=formato, cleanup=True)
    return caminho

def desenhar_arvore(raiz, nome_arquivo="arvore_binaria", formato="png"):
    """
    Gera uma imagem bonita da árvore binária usando Graphviz.
    """
    dot = Digraph(comment="Árvore Binária")

    # Layout da árvore
    dot.attr(rankdir="TB")  # Cima para baixo
    dot.attr('graph', bgcolor="#f9f9f9")  # Fundo clarinho
    dot.attr('node', shape="circle", style="filled", fontname="Helvetica", fontsize="12", color="#444444", fontcolor="white")

    # Paleta de cores para nós (vai alternando)
    cores = ["#4CAF50", "#2196F3", "#FF9800", "#9C27B0", "#F44336", "#00BCD4"]

    def adicionar(no, nivel=0):
        if not no:
            return
        cor = cores[nivel % len(cores)]
        dot.node(str(id(no)), label=str(no.dado), fillcolor=cor)

        if no.esquerda:
            dot.edge(str(id(no)), str(id(no.esquerda)), label="E", color="#666666", fontcolor="#666666")
            adicionar(no.esquerda, nivel + 1)

        if no.direita:
            dot.edge(str(id(no)), str(id(no.direita)), label="D", color="#666666", fontcolor="#666666")
            adicionar(no.direita, nivel + 1)

    adicionar(raiz)

    caminho = dot.render(filename=nome_arquivo, format=formato, cleanup=True)
    return caminho



if __name__ == "__main__":
    # Criando vértices
    passeio = Vertice("Passeio")
    diurno = Vertice("Diurno")
    frio = Vertice("Frio")
    planetario = Vertice("Planetário")
    museu = Vertice("Museu")
    calor = Vertice("Calor")
    parque = Vertice("Parque")
    praia = Vertice("Praia")

    noturno = Vertice("Noturno")
    restaurante = Vertice("Restaurante")
    cinema_noturno = Vertice("Cinema Noturno")

    # Vinculo dos filhos de Passeio
    passeio.esquerda = diurno
    passeio.direita = noturno

    # Vínculo dos filhos de diurno
    diurno.esquerda = frio
    diurno.direita = calor
    
    # Vinculo dos filhos de frio
    frio.esquerda = planetario
    frio.direita = museu

    # Vinculo dos filhos de calor
    calor.esquerda = parque
    calor.direita = praia

    # Vincula os filhos de noturno
    noturno.esquerda = restaurante
    noturno.direita = cinema_noturno

    # imprime representacao com parenteses
    print()
    print()

    print(passeio.representa_parenteses())

    # imprime representação com recuo
    print()
    print()
    print(passeio.representa_recuo())

    # imprime em ordem
    print()
    print()
    print(passeio.imprimir_ordem())

    # imprime em pré ordem
    print()
    print()
    print(passeio.imprimir_pre_ordem())

    # Imprimir em pós ordem
    print()
    print()
    print(passeio.imprimir_pos_ordem())

    # Desenho com graphviz
    caminho_png = desenhar_arvore(passeio, nome_arquivo="arvore_passeio", formato="png")
    print(f'\nFigura gerada: {caminho_png}')

