#include <stdio.h>
#include <string.h>

struct Aluno
{
    int numMatricula;
    char nome[30];
    char genero;  // sera exibido com %c
    int idade;
};

int main(){
    struct Aluno aluno1;
    struct Aluno aluno2;

    //Atribuindo valores aluno3 de acordo com os indices
    struct Aluno aluno3 = {3000, "Maria", 'M', 17};

    //inserindo dados aluno1
    aluno1.numMatricula = 1000;
    strcpy(aluno1.nome, "Joao");
    aluno1.genero = 'M';
    aluno1.idade = 18;

    // solicitando dados aluno2 ao usuario
    printf("\nInsira os dados do aluno2");
    printf("\nNome do aluno: ");
    scanf("%s", &aluno2.nome);

    printf("Numero de matricula: ");
    scanf("%d", &aluno2.numMatricula);

    printf("Genero: ");
    scanf("%s", &aluno2.genero);

    printf("Idade: ");
    scanf("%d", &aluno2.idade);



    //imprimindo dados aluno1
    printf("\nNome do alundo: %s", aluno1.nome);
    printf("\nNumero de matricula: %d", aluno1.numMatricula);
    printf("\nGenero: %c", aluno1.genero);
    printf("\nIdade: %d", aluno1.idade);
    printf("\n");

    printf("\nNome do aluno: %s", aluno2.nome);
    printf("\nMatricula: %d", aluno2.numMatricula);
    printf("\nGenero: %c", aluno2.genero);
    printf("\nIdade: %d", aluno2.idade);
    printf("\n");

    printf("\nNome do aluno: %s", aluno3.nome);
    printf("\nMatricula: %d", aluno3.numMatricula);
    printf("\nGenero: %c", aluno3.genero);
    printf("\nIdade: %d", aluno3.idade);
    return 0;
}