'''
Implementar uma lista encadeada em Python;

Implementar função count_nodes, que recebe uma lista encadeada
como parâmetro e retorna o número de nós presentes na lista encadeada;

Ao final do percurso, o valor do contador é retornado;

Adicionar elementos à lista encadeada usando o metodo append que será criado;
Em seguida, a função count_node é chamada passando a lista encadeada
como argumento, exibindo então o número de nós impresso na tela

'''

# Criando a classe Node que representa cada nó
# da lista encadeada;

class Node:
    def __init__(self, data):
        self.data = data  # Valor a ser armazenado no nó
        self.next = None  # Aponta para o próximo nó


# Criação da classe que representa a lista encadeada

class Lista_Encadeada:
    def __init__(self):
        self.head = None  # Head da lista que inicia vazia

    # Criação do método para adicionar elementos
    def append(self, data):
        new_node = Node(data)  # Cria um novo nó com dado que será fornecido
        if self.head is None:  # Condicional se a lista estiver vazia, adicione
            self.head = new_node
            return

        # se não estiver vazia, irá percorrer até o último node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node  # adição do novo node no final

    # Método para exibição da lista encadeada
    def exibir_lista(self):
        current = self.head
        if not current:
            print("A lista encadeada está vazia!")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Marca o fim da lista encadeada

# Função contadora de nodes da lista encadeada
def contador_nodes(linked_list):
    count = 0
    current = linked_list.head
    while current:  # loop que executa count enquanto houverem nós
        count += 1
        current = current.next
    return count

# Execução de testes
# Criação da lista encadeada

lista = Lista_Encadeada()

# Adição de elementos com método append
lista.append(10)
lista.append(20)
lista.append(30)
lista.append(40)
lista.append(50)

# Impressão da lista
print("Lista Encadeada:")
lista.exibir_lista()

# Executando contador de nodes passando a lista encadeada
# como argumento
node_count = contador_nodes(lista)
print(f'\nNúmero de nodes na Lista Encadeada: {node_count}')
