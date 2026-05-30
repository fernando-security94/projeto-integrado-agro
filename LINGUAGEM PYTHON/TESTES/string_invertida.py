# Testes com uma def que inverte caracteres
# de uma string
def reverse_string(texto):
    """
    Inverte os caracteres de uma string.

    >>> reverse_string("python")
    'nohtyp'

    >>> reverse_string("Jarvis")
    'sivraJ'

    >>> reverse_string("")
    ''

    """
    # ::-1 é uma slicing que inverte a s
    # o doctest valida diretamente os exemplos da docstring
    return texto[::-1]

# testes com assert
# Se houver algum erro, retornara AssertionError
assert reverse_string("python") == "nohtyp"
assert reverse_string("Jarvis") == "sivraJ"
assert reverse_string("") == ""

# testes com unittest
import unittest


class TestReverseString(unittest.TestCase):
    def test_word(self):
        self.assertEqual(reverse_string("python"), "nohtyp")

    def test_name(self):
        self.assertEqual(reverse_string("Jarvis"), "sivraJ")
    
    def test_empty(self):
        self.assertEqual(reverse_string(""), "")

if __name__ == '__main__':
    import doctest
    doctest.testmod()  # executa o doctest

    unittest.main(argv=[''], exit=False)

