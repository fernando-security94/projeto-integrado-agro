from graphviz import Digraph

# ---------------- Classe Filhos ----------------
class Filhos:
    """Classe para gerenciar múltiplos filhos de um vértice N-ário."""
    def __init__(self):
        self._vertices = []

    def representacao_com_parenteses(self):
        representacoes = []
        for vertice in self._vertices:
            representacoes.append(vertice.representacao_com_parenteses())
        return " ".join(representacoes)

    def representacao_com_recuo(self, numero_de_espacos=0):
        representacoes = []
        for vertice in self._vertices:
            representacoes.append(vertice.representacao_com_recuo(numero_de_espacos + 2))
        return "".join(representacoes)

    def inserir(self, dado):
        vertice_novo = Vertice(dado)
        self._vertices.append(vertice_novo)
        return vertice_novo

    def imprimir_percurso_pre_ordem(self):
        for vertice in self._vertices:
            vertice.imprimir_percurso_pre_ordem()

    def imprimir_percurso_pos_ordem(self):
        for vertice in self._vertices:
            vertice.imprimir_percurso_pos_ordem()


# ---------------- Classe Vertice ----------------
class Vertice:
    """Vértice de árvore N-ária."""
    def __init__(self, dado=None):
        self.dado = dado
        self.filhos = None

    def __str__(self):
        return str(self.dado)

    def representacao_com_parenteses(self):
        filhos = ""
        if self.filhos:
            filhos = self.filhos.representacao_com_parenteses()
        return "({} {})".format(str(self), filhos)

    def representacao_com_recuo(self, numero_de_espacos=0):
        filhos = ""
        if self.filhos:
            filhos = self.filhos.representacao_com_recuo(numero_de_espacos + 2)
        return "{}{}\n{}".format(" " * numero_de_espacos, str(self), filhos)

    def inserir_filho(self, dado):
        if self.filhos is None:
            self.filhos = Filhos()
        return self.filhos.inserir(dado)

    def imprimir_percurso_pre_ordem(self):
        print(self)
        if self.filhos:
            self.filhos.imprimir_percurso_pre_ordem()

    def imprimir_percurso_pos_ordem(self):
        if self.filhos:
            self.filhos.imprimir_percurso_pos_ordem()
        print(self)


# ---------------- Função para desenhar árvore N-ária ----------------
def desenhar_arvore_naria(raiz, nome_arquivo="arvore_naria", formato="png"):
    """
    Gera uma imagem da árvore N-ária usando Graphviz com cores diferentes por nível.
    """
    dot = Digraph(comment="Árvore N-ária")
    dot.attr(rankdir="TB")
    dot.attr('graph', bgcolor="#f9f9f9")
    dot.attr('node', shape="circle", style="filled", fontname="Helvetica", fontsize="12", color="#444444", fontcolor="white")

    cores = ["#4CAF50", "#2196F3", "#FF9800", "#9C27B0", "#F44336", "#00BCD4"]

    def adicionar(no, nivel=0):
        cor = cores[nivel % len(cores)]
        dot.node(str(id(no)), label=str(no.dado), fillcolor=cor)
        if no.filhos:
            for f in no.filhos._vertices:
                dot.edge(str(id(no)), str(id(f)))
                adicionar(f, nivel + 1)

    adicionar(raiz)
    caminho = dot.render(filename=nome_arquivo, format=formato, cleanup=True)
    return caminho


# ---------------- Exemplo de uso ----------------
if __name__ == "__main__":
    # Criação da árvore
    raiz = Vertice("Pacotes Turísticos")

    tranquilidade = raiz.inserir_filho("Tranquilidade")
    aventura = raiz.inserir_filho("Aventura")
    luxo = raiz.inserir_filho("Luxo")

    rafting = aventura.inserir_filho("Rafting")
    escalada = aventura.inserir_filho("Escalada")
    tirolesa = aventura.inserir_filho("Tirolesa")

    # Representações textuais
    print("\n--- Representação com recuo ---\n")
    print(raiz.representacao_com_recuo())

    print("\n--- Representação com parênteses ---\n")
    print(raiz.representacao_com_parenteses())

    # Percursos
    print("\n--- Pré-Ordem ---\n")
    raiz.imprimir_percurso_pre_ordem()

    print("\n--- Pós-Ordem ---\n")
    raiz.imprimir_percurso_pos_ordem()

    # Geração do gráfico colorido
    caminho_png = desenhar_arvore_naria(raiz, nome_arquivo="arvore_pacotes_turisticos", formato="png")
    print(f"\nFigura gerada: {caminho_png}")


"""
 No código, implementamos uma árvore n-ária, 
 onde cada vértice pode ter um número variável de filhos. 
 Inicialmente, criamos a raiz da árvore, que é um objeto da classe Vértice. 
 Diferentemente de uma árvore binária, que possui filhos esquerdo e direito, 
 na árvore n-ária, os vértices possuem uma lista de filhos, 
 representada pela estrutura de dados “list” do Python.

Para gerenciar essa lista de filhos, 
utilizamos a classe Filhos, que contém uma lista vazia. 
Essa classe é responsável por inserir novos vértices na árvore. 
O método Filhos.inserir() cria um novo objeto do tipo Vértice 
e o adiciona à lista usando list.append(). 
Os filhos são adicionados aos vértices por meio do método Vertice.inserir_filho(), 
que cria e retorna o vértice filho recém-criado (Takenaka, 2021).

A classe “Vertice”, por sua vez, é adaptada para acomodar a estrutura da árvore n-ária, 
substituindo os atributos esquerda e direita pelo atributo filhos. 
O método Vertice.inserir_filho() verifica se self.filhos está instanciado e, se não estiver, 
instancia um objeto da classe “Filhos”. 
Em seguida, delega a criação e inserção do novo vértice a self.filhos.inserir(). 
O método retorna o vértice filho criado, mantendo o processo de inserção 
transparente ao usuário da classe “Vertice”.

Essa abordagem permite a criação de uma árvore n-ária flexível e eficiente, 
onde cada vértice pode ter um número indefinido de filhos, 
facilitando a representação de estruturas de dados hierárquicas complexas.

"""