# ---------------- Classe Nó ----------------
class No:
    """Classe que representa um nó da árvore binária de busca."""
    def __init__(self, key):
        self.left = None   # Filho à esquerda
        self.right = None  # Filho à direita
        self.key = key     # Valor armazenado no nó


# ---------------- Classe Árvore Binária de Busca ----------------
class ArvoreBB:
    """Implementação de uma árvore binária de busca (BST)."""

    def __init__(self):
        self.root = None  # Raiz da árvore

    # ---- Inserção ----
    def inserir(self, key):
        """Insere um novo nó na árvore."""
        if self.root is None:
            self.root = No(key)
        else:
            self._inserir_recursivo(self.root, key)

    def _inserir_recursivo(self, current_No, key):
        """Insere recursivamente na subárvore correta."""
        if key < current_No.key:
            if current_No.left is None:
                current_No.left = No(key)
            else:
                self._inserir_recursivo(current_No.left, key)
        else:
            if current_No.right is None:
                current_No.right = No(key)
            else:
                self._inserir_recursivo(current_No.right, key)

    # ---- Remoção ----
    def remover(self, key):
        """Remove um nó da árvore, se existir."""
        self.root = self._remover_recursivo(self.root, key)

    def _remover_recursivo(self, current_No, key):
        """Remove recursivamente buscando a chave."""
        if current_No is None:
            return current_No

        if key < current_No.key:
            current_No.left = self._remover_recursivo(current_No.left, key)
        elif key > current_No.key:
            current_No.right = self._remover_recursivo(current_No.right, key)
        else:
            # Caso 1: sem filho à esquerda
            if current_No.left is None:
                return current_No.right
            # Caso 2: sem filho à direita
            elif current_No.right is None:
                return current_No.left
            # Caso 3: dois filhos -> substitui pelo menor valor da subárvore direita
            else:
                current_No.key = self._busca_valor_min(current_No.right)
                current_No.right = self._remover_recursivo(current_No.right, current_No.key)

        return current_No

    def _busca_valor_min(self, No):
        """Retorna o menor valor da subárvore."""
        while No.left is not None:
            No = No.left
        return No.key

    # ---- Busca ----
    def buscar(self, key):
        """Busca se um valor existe na árvore."""
        return self._busca_recursivo(self.root, key)

    def _busca_recursivo(self, current_No, key):
        """Busca recursiva."""
        if current_No is None or current_No.key == key:
            return current_No
        if key < current_No.key:
            return self._busca_recursivo(current_No.left, key)
        return self._busca_recursivo(current_No.right, key)

    # ---- Impressão (in-order traversal) ----
    def imprimir_em_ordem(self):
        """Imprime os elementos da árvore em ordem crescente."""
        elementos = []
        self._in_order(self.root, elementos)
        print("Árvore (in-order):", elementos)

    def _in_order(self, current_No, elementos):
        """Percorre a árvore em ordem e armazena os elementos."""
        if current_No is not None:
            self._in_order(current_No.left, elementos)
            elementos.append(current_No.key)
            self._in_order(current_No.right, elementos)


# ---------------- Exemplo de uso ----------------
bst = ArvoreBB()

# Inserindo nós
bst.inserir(3)
bst.inserir(1)
bst.inserir(4)
bst.inserir(2)

# Imprime a árvore em ordem
bst.imprimir_em_ordem()

# Verifica buscas
print("Tarefa prioridade -  1 existe?", bst.buscar(1) is not None)

# Remove e imprime de novo
print("Tarefa prioridade - 3 existe? Se sim, remover!", bst.buscar(3) is not None)
bst.remover(3)
bst.imprimir_em_ordem()
print("Tarefa prioridade 3 existe?", bst.buscar(3) is not None)








# Exemplo de binary search tree com impressao dos resultados
# in-order tranversal

# Criando a classe Nó
# class Node:
#     # Classe que representa um nó da Arvore Binária de busca
#     def __init__(self, key):
#         self.left = None    # filho à esquerda
#         self.right = None   # filho a direita
#         self.key = key      # filho armazenado no nó

    
# # Classe Arvore Binaria de Busca
# class BinarySearch:
#     # Implementação de uma Binary Search Tree
#     def __init__(self):
#         self.root = None    # raiz da arvore

#     # inserçao de nó
#     def inserir(self, key):
#         if self.root is None:
#             self.root = Node(key)
#         else:
#             self._inserir_recursivo(self.root, key)
        
    
#     def _inserir_recursivo(self, current_Node, key):
#         # Insere recursivamente na subárvore correta
#         if key < current_Node.key:
#             if current_Node.left is None:
#                 current_Node.left = Node(key)
#             else:
#                 self._inserir_recursivo(current_Node.right, key)

    
#     # Remoção
#     def remover(self, key):
#         # Remove um nó da árvore
#         self.root = self.remover._recursivo(self.root, key)
    
#     def _remover_recursivo(self, current_Node, key):
#         # Remove recursivamente buscando a chave
#         if current_Node is None:
#             return current_Node
        
#         if key < current_Node.key:
#             current_Node.left = self._remover_recursivo(current_Node.left, key)
#         elif key > current_Node.key:
#             current_Node.right = self._remover_recursivo(current_Node.right, key)
#         else:
#             # Caso 1: sem filho à esquerda
#             if current_Node.left is None:
#                 return current_Node.right
#             # Caso 2: sem filho à direita
#             elif current_Node.right is None:
#                 return current_Node.left
#             # Caso 3: Dois filhos -> Substitui pelo menor valor
#             # da subarvore à direia
#             else:
#                 current_Node.key = self._busca_valor_min(current_Node.right)
#                 current_Node.right = self._remover_recursivo(current_Node.right, current_Node.key)
#         return current_Node
    
    
#     def buscar_valor_min(self, Node):
#         # Retorna o menor valor da subárvore
#         while Node.left is not None:
#             Node = Node.left
#         return Node.key
    
#     # Busca se um valor existe na arvore
#     def buscar(self, key):
#         return self._busca_recursivo(self.root, key)
    
#     def _busca_recursivo(self, current_Node, key):
#         # Busca recursiva
#         if current_Node is None or current_Node.key == key:
#             return current_Node
#         if key < current_Node.key:
#             return self._busca_recursivo(current_Node.left, key)
#         return self._busca_recursivo(current_Node.right, key)
    
#     # Impressão in-order transversal
#     def imprimir_em_ordem(self):
#         # Imprime os elementos da arvore em ordem crescente
#         elementos = []
#         self._in_order(self.root, elementos)
#         print("Arvore (in-order): ", elementos)

#     def _in_order(self, current_Node, elementos):
#         # Percorre a arvore em ordem e armazena os elementos
#         if current_Node is not None:
#             self._in_order(current_Node.left, elementos)
#             elementos.append(current_Node.key)
#             self._in_order(current_Node.right, elementos)


# # Exemplos de uso
# bst = BinarySearch()

# # Inserindo nós
# bst.inserir(3)
# bst.inserir(1)
# bst.inserir(4)
# bst.inserir(2)

# # Imprimir arvore em ordem
# bst.imprimir_em_ordem