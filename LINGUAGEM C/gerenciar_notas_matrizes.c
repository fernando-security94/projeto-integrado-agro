// Criar gerenciamento de notas com matrizes
#include <stdio.h>
#define NUM_ALUNOS 3
#define NUM_DISCIPLINAS 3

 

int main(){

    float notas[NUM_ALUNOS][NUM_DISCIPLINAS] = 
    {{7.5, 8.0, 9.0}, {6.5, 7.0, 8.0}, {8.0, 7.5, 8.5}};

    float mediasAluno[NUM_ALUNOS];
    float mediaGeral, soma = 0;

    // calcula a media das notas de cada aluno em cada discplina
    for (int i = 0; i < NUM_ALUNOS; i++)
    {
        float soma = 0;
        for (int j = 0; j < NUM_DISCIPLINAS; j++)
        {
            soma += notas[i][j];
        }
        mediasAluno[i] = soma/NUM_DISCIPLINAS;
    }
    

    // Calcula media geral de cada aluno em todas disciplinas
    for (int i = 0; i < NUM_ALUNOS; i++)
    {
        soma += mediasAluno[i];
    }
    mediaGeral = soma/NUM_ALUNOS;

    // Exibe as medias de cada aluno em cada disciplina
    for (int i = 0; i < NUM_ALUNOS; i++)
    {
        printf("Media do aluno %d: %.2f\n", i+1, mediasAluno[i]);

    }

    // Exibe media geral de todos os alunos
    printf("Meida geral de todos os alunos: %.2f\n", mediaGeral);
    
    

    return 0;

}