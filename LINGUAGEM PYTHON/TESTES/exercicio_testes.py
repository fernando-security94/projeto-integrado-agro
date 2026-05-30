# Criar uma função que calcula a soma dos numeros
# em uma lista. Vamos realizar testes com:
# assertions, doctest e unittest

import doctest
import unittest

# Teste 1: Assertions
def sum_numbers(numbers):
    assert sum([1, 2, 3, 4]) == 10
    assert sum([-1, 0, 1]) == 0
    assert sum([]) == 0
    print("Todos os testes foram aprovados.")

    return sum(numbers)


teste = sum_numbers([1, 2, 3, 5])
print(teste)

# Teste 2: doctest
def sum_numbers(numbers):
    """
    >>> sum_numbers([1, 2, 3, 4])
    10

    >>> sum_numbers([-1, 0, 1])
    0

    >>> sum_numbers([])
    0
    
    """
    return sum(numbers)


"""print("Testes com doctest:\n")
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())"""

# Teste 3: Unittest

def sum_numbers(numbers):
    return sum(numbers)

class TestSumNumbers(unittest.TestCase):
    def test_sum_positives(self):
        self.assertEqual(sum_numbers([1, 2, 3, 4]), 10)

    def test_mixed_numbers(self):
        self.assertEqual(sum_numbers([-1, 0, 1]), 0)

    def test_sum_empty(self):
        self.assertEqual(sum_numbers([]), 0)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)