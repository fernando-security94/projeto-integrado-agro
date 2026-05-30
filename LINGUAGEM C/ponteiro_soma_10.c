// programa que contem um vetor de 5 inteiros
// ponteiro para inteiros
// associar o ponteiro ao primeiro vetor e somar mais 10 a cada vetor.

#include <stdio.h>

int main(){
    int vetor[5]= {1, 2, 3, 4, 5};

    int *ponteiro = vetor;  // associa ponteiro ao vetor

    // adiciona 10 em cada vetor enquanto i < 5
    for (int i = 0; i < 5; i++)
    {
        ponteiro[i] += 10;  // mesma coisa que *(ponteiro + i) += 10
    }

    printf("\nElementos do vetor apos add 10:\n");
    for (int i = 0; i < 5; i++)
    {
        printf("\n%d", vetor[i]);
    }
    printf("\n");


    
    return 0;
}