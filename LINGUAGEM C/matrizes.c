// Declarar uma matriz para armazenar notas
// do primeiro e segundo bimestre de tres alunos.
// No quadro 1, na linha 3, declaramos uma matriz "notas"
// com 3 linhas e 2 colunas, o que implica no armazenamento
// de 6 valores no total 
// (produto do numero de linhas pelo numero de colunas).
// Nas linhas 4 e 5, sao armazenadas as notas do primeiro aluno.
// É importante notar que as linhas (primeiro indice) permanecem
// fixas, enquanto as colunas (segundo indice) sao alteradas
// para registrar as notas dos respectivos alunos.
// Esse processo é repetido para o segundo e terceiro aluno,
// que sao armazenados na segunda e terceira linha da matriz,
// respectivamente.


// Para armazenar valores inseridos pelo usuario em uma matriz
// usamos scanf(), indicando os dois indices que selecionam a posicao
// na qual desejamos armazenar os valores, o mesmo vale para
// os elementos a serem impressos

#include <stdio.h>

int main(){
    
    float notas[3][2];

    // //aluno 1
    // notas[0][0];
    // notas[0][1];

    // //aluno 2
    // notas[1][0];
    // notas[1][1];

    // //aluno 3
    // notas[2][0];
    // notas[2][1] = 8.5;

    // printf("Digite uma nota: ");
    // scanf("%f", &notas[0][0]);
    // printf("Nota digitada: %.2f", notas[0][0]);

//  Forma otimizada
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            printf("Digite a nota %d do aluno %d: ", j+1, i+1);

            scanf("%f", &notas[i][j]);
        }
        
        printf("\n");  // quebra da linha para melhorar estética
    }
    

    return 0;
}