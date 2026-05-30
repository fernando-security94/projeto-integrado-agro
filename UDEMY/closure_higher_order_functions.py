"""
Higher Order Functions
Funções de primeira classe

Termos técnicos: Higher Order Functions e First-Class Functions

Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

    Higher Order Functions - Funções que podem receber e/ou retornar outras funções

    First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.

"""

"""
Closure e funções que retornam outras funções

"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar  # Função não executada será atribuida a variável apenas o local na memória do computador. 
# Forma de adiar a execução da função. Também é possível adiar a execução dos parâmetros, mudando para a função interna


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')


print(falar_bom_dia('Fernando'))  # Closure efetudado, com isso a função é executada e finalizada, 
print(falar_boa_noite('Poliane'))  # pelo fato do Python ter "lembrado" os valores dos parâmetros, 
                     # pois ja estavam salvos na memoria. 


# Laço for criado para executar a função com diversos valores iterados ao mesmo tempo. Aqui foi usado closure
for nomes in ['Arthur', 'Tamires', 'Felipe', 'Fábio', 'Edna']:
    print(falar_bom_dia(nomes))
    print(falar_boa_noite(nomes))




"""
Closure de função com adiamento de execução de argumento. Nesse caso, somente o parâmetro saudacao será lembrado
e o nome será dinâmico

Desse jeito, o parâmetro nome foi para a função interna saudar(), ou seja, sua execução foi adiada
e só será relizada no momento do closure, passando seu valor.

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar  


saudacao_1 = criar_saudacao('Bom dia')
saudacao_2 = criar_saudacao('Boa noite')

print(saudacao_1('Fernando)) 
print(saudacao_2(Poliane))

"""