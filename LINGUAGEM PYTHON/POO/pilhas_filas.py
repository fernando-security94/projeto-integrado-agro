# Exemplos de pilhas

pilha = [4, 1, 5, 1, 6]
print(pilha)

pilha.append(10)
print(pilha)

pilha.pop(1)  # posso remover itens a partir do índice ou apenas o último com pop
print(pilha)

# Exemplo de pilhas

class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items.append(item)
    
    def desempilhar(self):
        self.items.pop()
        return None
    
my_stack = Pilha()
my_stack.empilhar(1)
my_stack.empilhar(2)
my_stack.empilhar(3)
my_stack.empilhar(4)
print(f'\nItens na fila: {my_stack.items}')

my_stack.desempilhar()
print(f'\nItens na fila após desempilhar: {my_stack.items}')
print()

# exemplo de pilhas em linked lists

class Item:
    def __init__(self, valor=None, anterior=None):
        self.valor = valor
        self.anteiror = anterior
    
    def __repr__(self):
        return "%s\n%s"%(self.valor, self.anteiror)
    
# Implementando class Pilha

class Pilhas:
    def __init__(self):
        self.topo = None
    
    def __repr__(self):
        return "Topo\n%s\nRodapé"%(self.topo)
    
    def push(self, valor):
        # cria novo objeto item
        item_novo = Item(valor)

        # anterior passa a ser o antigo topo
        item_novo.anteiror = self.topo

        # o topo da pilha passa a ser o item novo
        self.topo = item_novo
    
    def popping(self):
        # assert verifica se o topo da pilha esta vazio, se sim, retorna erro, se nao, altera o valor do topo
        assert self.topo, "Erro: Pilha vazia!"
        self.topo = self.topo.anteiror

# Exemplo de utilização

pilha = Pilhas()
pilha.push('a')
pilha.push('b')
pilha.push('c')
pilha.push('d')
print(pilha)
print()

pilha.popping()
print(pilha)
print()

from collections import deque
fila = deque(['banana', 'chocolate', 'morango'])
print(fila)
fila.append('abacaxi')
print(f'Fila após adicionar item: {fila}')
print()

fila.appendleft('açúcar')  # adiciona item em primeiro lugar
print(f'Fila após appendleft: {fila}')


fila.popleft()  # remove item à esquerda, ao contrário de pop()
fila.popleft()
print(f'\nFila após dois popleft: {fila}')


# Exercicio de fila com listas encadeadas

class Node:
    def __init__(self, id):
        self.id = id
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None



    def inqueue(self, id):
        new_node = Node(id)

        if self.tail:
            self.tail.next = new_node
        
        if not self.head:
            self.head = new_node

    def offqueue(self):
        if not self.head:
            return None
        
        removed_id = self.head.id
        self.head = self.head.next

        if not self.head:
            self.tail = None
        
        return removed_id

# Exemplo de uso
process_queue = Queue()
process_queue.inqueue(1)
process_queue.inqueue(2)
process_id = process_queue.offqueue()
print(process_id)

'''
Nesse código, a classe Node representa cada demanda na fila, 
enquanto a classe Queue gerencia a fila de processos. 
O método inqueue adiciona novas demandas ao fim da fila, 
e o método offqueue remove a demanda mais antiga do início da fila. 
Essa implementação garante que a ordem das demandas seja mantida e que a 
manipulação da fila seja feita de maneira eficiente, 
adequando-se ao aumento do volume de trabalho após a fusão da empresa.


'''