from listas_encadeadas import ListaEncadeada as le

# criação do objeto
lista = le()
print("Conteúdo da lista: ", lista)  # Retornará None por estar vazia

# Adicionando elementos na lista
lista.insere(lista, "shampoo")
lista.insere(lista, "biscoito")
lista.insere(lista, "detergente")
lista.insere(lista, "abobrinha")
lista.insere(lista, "banana")

print("\nConteúdo da lista atualizado: ", lista)

# Execução de buscar elementos diretamento no print
print("\nBuscar 'detergente': ", lista.buscar("detergente"))
print("Buscar 'alface': ", lista.buscar("alface"))

# Execução de contagem de elementos da lista diretamente no print
print("\nNúmero de itens na lista: ", lista.contar())


# Execução de remover elementos da lista
lista.remover("biscoito")
print("\nConteúdo da lista após remoção: ", lista)

print("\nNúmero de itens atualizado: ", lista.contar())
