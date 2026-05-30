'''
O problema é desenvolver um sistema de avaliação de desempenho 
que possa avaliar automaticamente as notas dos alunos em várias disciplinas
e determinar se eles passaram ou falharam de acordo com as regras da escola.

Para vencer esse desafio, você aprenderá nesta seção 
os conteúdos referentes aos métodos dedutíveis e à lógica proposicional 
que irão te auxiliar no desenvolvimento de estudo de caso e torná-lo um grande desenvolvedor.

Definição de critérios de avaliação: 
A equipe de desenvolvimento começa definindo os critérios de avaliação para cada disciplina. 
Por exemplo, pode ser definido que um aluno precisa obter uma média de pelo menos 5,0 em Matemática para ser aprovado.

Modelagem de fórmulas lógicas: para cada disciplina
são definidas fórmulas lógicas que especificam os critérios de aprovação. 

Por exemplo, "Média em Matemática >= 5,0" é uma fórmula que determina se um aluno passou em Matemática.

Entrada de notas: 
os professores inserem as notas dos alunos em um sistema computacional 
que calcula automaticamente a média e aplica as fórmulas lógicas correspondentes.

Valoração de fórmulas lógicas: 
o sistema avalia as fórmulas lógicas para cada disciplina com base nas notas do aluno. 

Se todas as fórmulas são verdadeiras, o aluno é aprovado na disciplina; caso contrário, é reprovado.

Emissão de relatórios: 
o sistema gera automaticamente relatórios de aprovação ou reprovação para cada aluno, 
com base nas valorações das fórmulas lógicas. Os relatórios podem ser impressos 
e entregues aos alunos e seus responsáveis.
Testes e verificação: a equipe realiza testes para garantir 
que o sistema avalie corretamente as notas e aplique as fórmulas lógicas de acordo com as regras da escola.

'''


report_card = ''
media_matematica = input('Nota de Matemática: ')
media_portugues = input('Nota de Portugues: ')
media_ciencias = input('Nota de Ciencias: ')

print()

if media_matematica >= '5':
    print(f'Approved, grade: {media_matematica}')
elif media_matematica > '10':
    print("Grade higher than 10 is not supported")
elif media_matematica < '0':
    print('Negative grade is not supported')
else:
    print(f'Not approved, grade:{media_matematica}')
    print(report_card)
    
print(report_card)   

if media_portugues >= '5' :
    print(f'Approved, grade: {media_portugues}')
elif media_portugues > '10':
    print('Grade higher than 10 is not supported')
elif media_portugues < '0':
    print('Negative grade is not supported')
    
else:
    print(f'Not approved, grade: {media_portugues}')       

print()

if media_ciencias >= '5':
    print(f'Approved, grade: {media_ciencias}')
elif media_ciencias > '10':
    print('Grade higher than 10 is not supported')
elif media_ciencias < '0':
    print('Negative grade is not supported')
    
else:
    print(f'Not approved, grade:{media_ciencias}')       
    print()
print()