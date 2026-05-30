'''Seu objetivo é criar um sistema em Python 
que utilize uma árvore AVL para organizar uma lista de contatos, 
permitindo operações eficientes de adição, remoção e busca de contatos por nome.

Especificações:

Estrutura do contato: cada contato deve ser um objeto contendo id (inteiro único), 
nome (string) e telefone (string). O id servirá como chave para a organização na árvore AVL.
Adição de contatos: o sistema deve suportar a adição de novos contatos, 
mantendo a árvore AVL balanceada após cada inserção.
Remoção de contatos: deve ser possível remover contatos usando o id como referência, 
assegurando o balanceamento da árvore após cada remoção.
Busca de contatos: o sistema deve permitir a busca de contatos por nome, 
retornando todas as correspondências encontradas.
Boa prática!

Para assimilar todo o conteúdo visto, deixamos algumas perguntas para reflexão:

Como a escolha entre uma árvore de busca binária e uma árvore AVL 
pode impactar o desempenho de um sistema de gerenciamento de banco de dados?
De que maneira as árvores B e Quadtrees são especialmente úteis para aplicações 
que envolvem o processamento de grandes volumes de dados e dados espaciais?
Qual a importância do balanceamento em árvores AVL e como isso influencia 
a eficiência das operações de busca, inserção e remoção?'''


# avl_agenda.py
# ========================================================
# Estrutura de Árvore AVL aplicada a uma Agenda de Contatos
# ========================================================

class Contato:
    """Representa um contato simples com id, nome e telefone."""

    def __init__(self, id, nome, telefone):
        self.id = id
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Telefone: {self.telefone}"


class NodoAVL:
    """Nó da árvore AVL, armazenando um contato."""

    def __init__(self, contato):
        self.contato = contato
        self.altura = 1  # Altura inicial (folha)
        self.esquerdo = None
        self.direito = None


class AgendaAVL:
    """Árvore AVL para gerenciar contatos de forma balanceada."""

    def __init__(self):
        self.raiz = None

    # ---------- Funções utilitárias ----------
    def _altura(self, nodo):
        """Retorna a altura do nodo (0 se None)."""
        return nodo.altura if nodo else 0

    def _fator_balanceamento(self, nodo):
        """Calcula o fator de balanceamento (esq - dir)."""
        if not nodo:
            return 0
        return self._altura(nodo.esquerdo) - self._altura(nodo.direito)

    def _rotacao_direita(self, y):
        """Rotação simples à direita."""
        x = y.esquerdo
        T2 = x.direito

        # Rotaciona
        x.direito = y
        y.esquerdo = T2

        # Atualiza alturas
        y.altura = 1 + max(self._altura(y.esquerdo), self._altura(y.direito))
        x.altura = 1 + max(self._altura(x.esquerdo), self._altura(x.direito))

        return x

    def _rotacao_esquerda(self, x):
        """Rotação simples à esquerda."""
        y = x.direito
        T2 = y.esquerdo

        # Rotaciona
        y.esquerdo = x
        x.direito = T2

        # Atualiza alturas
        x.altura = 1 + max(self._altura(x.esquerdo), self._altura(x.direito))
        y.altura = 1 + max(self._altura(y.esquerdo), self._altura(y.direito))

        return y

    # ---------- Inserção ----------
    def adicionar(self, contato):
        """Insere um contato na agenda."""
        self.raiz = self._adicionar(self.raiz, contato)

    def _adicionar(self, nodo, contato):
        if not nodo:
            return NodoAVL(contato)

        if contato.id < nodo.contato.id:
            nodo.esquerdo = self._adicionar(nodo.esquerdo, contato)
        elif contato.id > nodo.contato.id:
            nodo.direito = self._adicionar(nodo.direito, contato)
        else:
            # IDs duplicados não são permitidos
            return nodo

        # Atualizar altura
        nodo.altura = 1 + max(self._altura(nodo.esquerdo), self._altura(nodo.direito))

        # Verificar balanceamento
        balance = self._fator_balanceamento(nodo)

        # Casos de desbalanceamento
        if balance > 1 and contato.id < nodo.esquerdo.contato.id:
            return self._rotacao_direita(nodo)

        if balance < -1 and contato.id > nodo.direito.contato.id:
            return self._rotacao_esquerda(nodo)

        if balance > 1 and contato.id > nodo.esquerdo.contato.id:
            nodo.esquerdo = self._rotacao_esquerda(nodo.esquerdo)
            return self._rotacao_direita(nodo)

        if balance < -1 and contato.id < nodo.direito.contato.id:
            nodo.direito = self._rotacao_direita(nodo.direito)
            return self._rotacao_esquerda(nodo)

        return nodo

    # ---------- Remoção ----------
    def remover(self, id):
        """Remove um contato pelo ID."""
        self.raiz = self._remover(self.raiz, id)

    def _remover(self, nodo, id):
        if not nodo:
            return nodo

        if id < nodo.contato.id:
            nodo.esquerdo = self._remover(nodo.esquerdo, id)
        elif id > nodo.contato.id:
            nodo.direito = self._remover(nodo.direito, id)
        else:
            # Encontrou o nodo a remover
            if not nodo.esquerdo:
                return nodo.direito
            elif not nodo.direito:
                return nodo.esquerdo

            # Substitui pelo menor da subárvore direita
            temp = self._minimo(nodo.direito)
            nodo.contato = temp.contato
            nodo.direito = self._remover(nodo.direito, temp.contato.id)

        if not nodo:
            return nodo

        # Atualizar altura
        nodo.altura = 1 + max(self._altura(nodo.esquerdo), self._altura(nodo.direito))

        # Balancear
        balance = self._fator_balanceamento(nodo)

        if balance > 1 and self._fator_balanceamento(nodo.esquerdo) >= 0:
            return self._rotacao_direita(nodo)

        if balance > 1 and self._fator_balanceamento(nodo.esquerdo) < 0:
            nodo.esquerdo = self._rotacao_esquerda(nodo.esquerdo)
            return self._rotacao_direita(nodo)

        if balance < -1 and self._fator_balanceamento(nodo.direito) <= 0:
            return self._rotacao_esquerda(nodo)

        if balance < -1 and self._fator_balanceamento(nodo.direito) > 0:
            nodo.direito = self._rotacao_direita(nodo.direito)
            return self._rotacao_esquerda(nodo)

        return nodo

    def _minimo(self, nodo):
        """Encontra o nodo de menor ID."""
        atual = nodo
        while atual.esquerdo:
            atual = atual.esquerdo
        return atual

    # ---------- Busca ----------
    def buscar_por_nome(self, nome):
        """Retorna lista de contatos que possuem o nome informado."""
        resultados = []
        self._buscar_por_nome(self.raiz, nome.lower(), resultados)
        return resultados

    def _buscar_por_nome(self, nodo, nome, resultados):
        if nodo:
            if nome in nodo.contato.nome.lower():
                resultados.append(nodo.contato)
            self._buscar_por_nome(nodo.esquerdo, nome, resultados)
            self._buscar_por_nome(nodo.direito, nome, resultados)

    def buscar_por_telefone(self, telefone):
        """Retorna contato exato pelo telefone (ou None)."""
        return self._buscar_por_telefone(self.raiz, telefone)

    def _buscar_por_telefone(self, nodo, telefone):
        if not nodo:
            return None
        if nodo.contato.telefone == telefone:
            return nodo.contato
        # busca em ambos os lados
        achado = self._buscar_por_telefone(nodo.esquerdo, telefone)
        if achado:
            return achado
        return self._buscar_por_telefone(nodo.direito, telefone)

    # ---------- Impressão ----------
    def imprimir(self):
        """Imprime todos os contatos em ordem crescente de ID."""
        self._imprimir(self.raiz)

    def _imprimir(self, nodo):
        if nodo:
            self._imprimir(nodo.esquerdo)
            print(nodo.contato)
            self._imprimir(nodo.direito)


# -------------------------------
# Testes práticos
# -------------------------------
if __name__ == "__main__":
    agenda = AgendaAVL()

    # Inserção
    agenda.adicionar(Contato(3, "Alice", "1111-1111"))
    agenda.adicionar(Contato(1, "Bob", "2222-2222"))
    agenda.adicionar(Contato(2, "Carlos", "3333-3333"))
    agenda.adicionar(Contato(4, "Diana", "4444-4444"))

    print("\nAgenda após inserção:")
    agenda.imprimir()

    # Busca
    print("\nBusca por nome 'Alice':", [str(c) for c in agenda.buscar_por_nome("Alice")])
    print("Busca por telefone '3333-3333':", agenda.buscar_por_telefone("3333-3333"))

    # Remoção
    agenda.remover(2)
    print("\nAgenda após remover ID=2:")
    agenda.imprimir()
