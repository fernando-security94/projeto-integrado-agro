# funcao que retorna numero primo

def num_primo(numero):
    """
    Retorna True se o número for primo, senão False

    >>> num_primo(2)
    True
    
    >>> num_primo(4)
    False
    
    >>> num_primo(17)
    True
    
    >>> num_primo(1)
    False
    
    >>> num_primo(0)
    False
    
    """
    if numero < 2:  # 2 é o menor número primo
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# testes com assert
assert num_primo(2) == True
assert num_primo(4) == False
assert num_primo(17) == True
assert num_primo(1) == False

# testes com unittest
import unittest

class TestNumPrimo(unittest.TestCase):
    def test_num_2(self):
        self.assertEqual(num_primo(2), True)
    
    def test_num_4(self):
        self.assertEqual(num_primo(4), False)

    def test_num_17(self):
        self.assertEqual(num_primo(17), True)

    def test_num_1(self):
        self.assertEqual(num_primo(1), False)


# unittest do chatGPT, que separa em duas def
# uma def somente para num_primo que retornem True, e a outra para False
# class TestNumPrimo(unittest.TestCase):
#     def test_primo_true(self):
#         self.assertEqual(num_primo(2), True)
#         self.assertEqual(num_primo(17), True)

#     def test_primo_false(self):
#         self.assertEqual(num_primo(4), False)
#         self.assertEqual(num_primo(1), False)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    unittest.main(argv=[''], exit=False)

"""
Lógica do numero primo:
✅ O que é um número primo?
Um número primo:

É maior ou igual a 2.

Só tem dois divisores: 1 e ele mesmo.

Exemplos:
2, 3, 5, 7, 11, 13... OBS: todo numero que termina com 1, 3, 5, 7, 
O 4, por exemplo, não é primo porque pode ser dividido por 2.


for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
        return False

Explicação:        
Por que começamos do 2?
O 1 divide tudo, então não precisamos testar ele.

Por que vamos até a raiz quadrada de numero?
Essa é a parte mais matematicamente inteligente da função.
👉 Se numero não for primo, ele terá um divisor entre 2 e √numero.

Vamos supor numero = 49
A raiz de 49 é 7.
Os divisores de 49 são: 1, 7, 49
Logo, se ele tiver algum divisor entre 2 e 7, sabemos que não é primo.

Se testássemos até 49, seria lento.
Testando só até √49 + 1 (ou seja, até 7), já é suficiente.
O mesmo vale para numero = 97 → basta testar até √97 ≈ 9.8, ou seja, até 10.

.

🚀 Resumo da lógica matemática:
Se um número tem algum divisor além de 1 e ele mesmo, ele não é primo.

Se não tem nenhum divisor entre 2 e √n, ele é primo.

Isso otimiza bastante o código (economiza laços desnecessários).

✅ Um número é primo se ele só pode ser dividido exatamente (sem sobra) por 1 e ele mesmo.
Ou seja:

Se tiver qualquer outro divisor além de 1 e dele mesmo, não é primo.

A verificação if numero % i == 0 dentro do for serve justamente para detectar se existe algum outro divisor.


Sobre o range(2, int(numero**0.5) + 1):
A ideia de verificar até a raiz quadrada do número 
é um atalho matemático para economizar verificações, porque:
Se numero tiver um divisor, um dos dois fatores sempre 
será menor ou igual à raiz quadrada dele.

Por exemplo: se 25 = 5 * 5 → o divisor 5 aparece até √25.

Destrinchando o codigo por partes:

range(2, int(numero**0.5) + 1)
Esse código é usado para verificar se um número tem algum divisor 
entre 2 e a raiz quadrada de numero (inclusive). Vamos entender o que faz cada parte:

🔹 numero ** 0.5
Isso é o mesmo que tirar a raiz quadrada de um número.

Exemplo:

numero = 25
numero ** 0.5 = 5.0  (**0.5 = raiz quadrada)


🔹 int(numero ** 0.5)
A raiz quadrada pode ser um número decimal. 
Como range() só aceita inteiros, usamos int() para converter:

int(5.0) = 5
int(6.4) = 6
Note: o int() corta a parte decimal (não arredonda), ou seja, trunca.

🔹 int(numero ** 0.5) + 1
O +1 é necessário porque o range() não inclui o limite superior.

Então se fizermos:
range(2, 5)  → 2, 3, 4   (não inclui o 5)

Mas queremos testar até o número da raiz quadrada incluída. Por isso:

range(2, int(numero ** 0.5) + 1)


Outro exemplo:

numero = 29
numero ** 0.5        = 5.385...
int(numero ** 0.5)   = 5
int(...) + 1         = 6
range(2, 6)          = [2, 3, 4, 5]
Vamos tentar dividir 29 por 2, 3, 4 e 5. Nenhum funciona → então 29 é primo ✅








"""