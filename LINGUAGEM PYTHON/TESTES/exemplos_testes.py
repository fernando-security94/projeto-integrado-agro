# testes em uma lista que calcula a média
# dos valores

import unittest
import doctest

# Exemplo de doctest
# Doctest: Os exemplos dentro da docstring serão usados como teste automático.
# Utilizado para documentação viva: exemplos que testam
def media(lista):
    """
    Calcula a média de uma lista de números
    >>> media([10, 20, 30])
    20.0

    >>> media([1, 2, 3, 4])
    2.5

    >>> media([])
    0

    """

    if not lista:
        return 0
    return sum(lista) / len(lista)

print("Testes usando Doctest:\n")
print(doctest.testmod())
print()

# Teste com ASSERT são rápidos e recomendados
# protótipos ou validações simples.
assert media([10, 20, 30]) == 20.0
assert media([1, 2, 3, 4]) == 2.5
assert media([]) == 0
print("Todos os testes passaram!")


# Teste com unittest -  Testes mais robustos, organizados
# e escaláveis
class TestMedia(unittest.TestCase):
    def test_lista_normal(self):
        self.assertEqual(media([10, 20, 30]), 20.0)
    
    def test_lista_simples(self):
        self.assertEqual(media([1, 2, 3, 4]), 2.5)

    def test_empty(self):
        self.assertEqual(media([]), 0)

# executando os testes com if __name__ == '__main__'
import doctest
if __name__ == '__main__':
    doctest.testmod()  # executa os testes de da docstring

    unittest.main(argv=[''], exit=False)  # executa o unittest

"""
Método | Vantagens | Ideal para

assert | Simples, direto | Testes rápidos durante o dev
doctest | Documentação + Teste | Mostrar exemplos no docstring
unittest | Estrutura robusta, relatórios | Projetos maiores e produção


"""

