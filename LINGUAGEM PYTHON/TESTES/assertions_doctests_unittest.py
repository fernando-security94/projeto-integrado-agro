# Exemplos de testes em python com 
# assertions, doctests e unittests

# Assertions- expressoes utilizadas
# para verificar condições verdade durante a execução do codigo
# são fundamentais para detecção de erros e bugs.

import doctest
import unittest

def divide(x, y):
    assert y != 0  # se o test for True, retornará AssertionError

    return x/y

result = divide(6, 2)
print(result)  # AssertionError: Divisão por zero!
print()

# Mais testes com assert

def square(x):
    return x * x 

assert square(3) == 9
assert square(-2) == 4
assert square(0) == 0

print("Todos os asserts passaram!\n")


# Doctest permite incorporar testes 
# diretamente na documentação do código.
# A função abaixo retorna o quadrado de um numero
def square(x):
    """   
    >>> square(3)  # >>> indica que é um bloco de codigo Python
    9
    >>> square(-2)
    4
    >>> square(0)
    0
    """
    return x * x

print("Testes usando doctest:")
print(doctest.testmod())
print()

# Utilizando unittest, que realiza os testes
# atraves de classes

def square(x):
    return x * x

class TestSquareFunction(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(square(3), 9)

    def test_negative(self):
        self.assertEqual(square(-2), 4)

    def test_zero(self):
        self.assertEqual(square(0), 0)

# if __name__ == '__main__':  # se esse bloco for executado, o código será encerrado aqui
#     unittest.main()
print()

# Exemplo 2 Unittest
def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2,3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2,-3), -5)

print()


# teste unittest 3
def division(x, y):
    if y == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    else:
        return x/y

class TestDivision(unittest.TestCase):
    def test_division_positives(self):
        self.assertEqual(division(10, 2), 5)
    
    def test_division_negatives(self):
        self.assertEqual(division(-20, -5), 4)
    
    # def test_divisio_zero(self):
    #     with self.assertRaises(ZeroDivisionError):
    #         division(20, 0)

if __name__ == '__main__':  
    import unittest
    unittest.main(argv=[''], exit=False)
    print()

"""
A função add simplesmente soma dois números e 
cria uma classe que herda de unittest.TestCase. 
Isso indica que essa classe contém testes unitários. 
Dentro da classe de teste, você define métodos de teste. 
Cada método de teste deve começar com a palavra-chave test. 
Dentro desses métodos, você usa assertivas (como self.assertEqual) 
para verificar se o comportamento esperado do código é atendido. 
A condição if __name__ == '__main__': garante que a suíte de testes 
seja executada somente se o script for executado diretamente 
(não se for importado como um módulo em outro script). unittest.main() 
executa todos os testes definidos na classe TestAddition.
"""

"""
Dica: para evitar que o unittest capture argumentos 
do Jupyter ou terminal, adicione unittest.main(argv=[''], exit=False) ]
quando estiver rodando fora de arquivos .py.
"""

"""
A função square é acompanhada por uma string de documentação que inclui exemplos de uso.
Esses exemplos estão formatados de maneira especial, usando o prompt >>>, 
que indica um bloco de código Python.
Quando você executa doctest.testmod(), o módulo doctest procura 
todas as strings de documentação no seu código que contenham blocos de código >>> 
e executa esses blocos como testes. Ele compara a saída real desses blocos 
com o resultado esperado fornecido nos comentários.
No caso do exemplo anterior, doctest.testmod() executará a função square(3) 
e verificará se o resultado é igual a 9, executará square(-2) e verificará se o resultado é 4, e assim por diante.
Se todos os testes passarem, o doctest não produzirá nenhuma saída. S
e houver uma discrepância entre a saída real e a esperada, o doctest imprimirá uma mensagem indicando 
onde ocorreu o problema. A principal vantagem do doctest é que ele permite que você mantenha 
exemplos na documentação e, ao mesmo tempo, os utilize como testes automatizados. 
Isso ajuda a garantir que a documentação esteja sempre em sincronia com o código real. 
Além disso, quando você executa os testes, obtém uma validação automática 
dos exemplos apresentados na documentação.

"""


"""
Em quais casos o argv em unittest vira vazio com '' ou 'ignore-first-...'


ChatGPT said:
Excelente pergunta! O parâmetro argv em unittest.main() 
é usado para controlar os argumentos passados ao rodar o script, e isso impacta diretamente 
como o unittest interpreta a linha de comando. Aqui está o resumo claro de quando e por que usamos cada um:

✅ 1. argv=[''] → mais comum em notebooks / IDEs
Uso principal: evitar que o Jupyter Notebook, o VS Code, ou qualquer ambiente com argumentos de linha de comando próprios atrapalhe a execução do unittest.

Ele impede que o unittest.main() tente interpretar argumentos externos como opções de teste.

python
Copy
Edit
unittest.main(argv=[''], exit=False)
exit=False evita que o notebook pare de executar após os testes.

✅ 2. argv=['first-arg-is-ignored'] → equivalente funcional
Essa forma é usada quando você quer ignorar o primeiro argumento, 
que normalmente é o nome do script (sys.argv[0]), e deixar o restante vazio.

Funciona do mesmo jeito em ambientes interativos como notebooks, mas a string é só um "placeholder".
unittest.main(argv=['first-arg-is-ignored'], exit=False)

🧠 Por que isso é necessário?
Quando você roda um script fora de um terminal, como em Jupyter, IDLE, ou em um script importado, o unittest.main() pode tentar ler argumentos que não fazem parte do seu teste (e isso causa erro). Então, a gente "zera" os argumentos com argv=[''] ou ignora o primeiro com ['first-arg-is-ignored'].

✅ Resumo prático

Forma	Situação de uso
argv=['']	Mais comum em notebooks / IDEs
argv=['first-arg-is-ignored']	Alternativa funcional (semântica)
unittest.main() normal	Ao rodar diretamente no terminal


"""