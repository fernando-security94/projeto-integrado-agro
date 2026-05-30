// conceito de ponteiros
// ponteiros para estruturas de dados



// Começando com as structs, 
// ponteiros para estruturas são escritos 
// de forma similar a uma variável comum. 
// A principal diferença 
// é o uso do operador “->” para acesso aos membros


#include <stdio.h>
#include <string.h>


// ponteiros em structs
struct aluno
{
    int materia;
    float nota;
};


int main(){
    struct aluno joao;
    struct aluno *ponteiro;  // declacarao do ponteiro para struct

    // inicializacao struct declarada
    joao.materia = 1000;
    joao.nota = 8.5;

    //inicializacao do ponteiro
    ponteiro = &joao;

    //impressao do atrirbuto materia atraves do ponteiro
    printf("%d", ponteiro->materia);

    // impressao do atributo nota atraves do ponteiro
    printf("\n%.2f", ponteiro->nota);
    printf("\n");

//exemplo de ponteiro para vetor
    char *ponteiro2;

    int i;

    char vetor[5] = {'a', 'b', 'c', 'd', 'e'};

    ponteiro2 = vetor;  // variavel ponteiro ponteiro2 aponta para o primeiro elemento de vetor.

    for (i = 0; i < 5; i++)
    // conteudo do vetor acessado pela variavel
    {
        printf("\nVetor[%d] = %c", i, vetor[i]);

        // conteudo do vetor acessado pelo ponteiro
        printf("\nPonteiro: %c", *ponteiro2);

        ponteiro2++;
    }

    return 0;

}