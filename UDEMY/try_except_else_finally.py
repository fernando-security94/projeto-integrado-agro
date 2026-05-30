"""
Try, except, else e finally

"""

# a = 18
# b = 0
# c = a / b


try:
    a = 18
    b = 0
    print(b[0])
    print('Linha 1'[1000])
    c = a / b
except ZeroDivisionError:
    print('Divisão por zero!')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:  # Atribuindo as duas exceções em uma variável
    print('TypeError + IndexError')
    print('MSG:', error)  # Exibe a mensagem de acordo com o tipo de erro
    print('Nome:', error.__class__.__name__)  # Exibe o nome específico do erro.
except Exception as unknow:
    print('ERRO DESCONHECIDO')
    print(unknow.__class__.__name__)
finally:
    print('Programa encerrado')

print()
  
# Quando for try finally, o finally sempre será executado, mesmo
# se tiver algum erro. O erro será exibido após finally ser executado

try:
    print('ABRIR ARQUIVO')
    8/0
    print(1234)
except ZeroDivisionError as e:  # Tratando a exceção antes de executar para nao ser levantado após o fechamento
    print(e.__class__.__name__)
    print(e)
    print('Dividiu por zero')
except IndexError as error:
    print('Index error')
except (NameError, ImportError):
    print('NameError', 'ImportError')
else:
    print('Não deu erro')  # Será executado quando não houver erro
finally:
    print(5678)
    print('FECHAR ARQUIVO')

"""
No bloco try, except, else, finally temos diversos
tratamentos de exceções que podem ser levantadas quando o código
for executado, sendo cada uma específica de um tipo de objeto.

Se ao fim do bloco, ainda tiver um erro que não saiba qual seja, podemos usar
except Exception para encontrar o tipo de erro.

Para exibir o tipo de erro e a mensagem, atribuiumos o erro
à uma variável qualquer e usamos .__class.__name. Ex:
Except NameError as error:
    print(error.__class.__name__)

Podemos usar else depois de que todas as exceções forem tratadas,
e se não houverem erros, o else será executado, ja o finally,
será executado com ou sem erros, podendo tornar o código
reduntante.

Blocos permitidos:

Try:
Except:

Try:
Finally:

Try:
Except:
else:

Try:
Except:
Finally:

Try:
except:
else:
Finally

"""


