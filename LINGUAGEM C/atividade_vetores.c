#include <stdio.h>
#include <string.h>
#include <math.h>

int main(){
    //declarando vetor de 5 inteiros
    int vetor[5];
    
    //entrada de dados pelo usuário
    int primeiro_elemento = vetor[0];
    printf("\nDigite o primeiro elemento: ");
    scanf("%d", &primeiro_elemento);

    int segundo_elemento = vetor[1];
    printf("\nDigite o segundo elemento: ");
    scanf("%d", &segundo_elemento);

    int terceiro_elemento = vetor[2];
    printf("\nDigite o terceiro elemento: ");
    scanf("%d", &terceiro_elemento);

    int quarto_elemento = vetor[3];
    printf("\nDigite o quarto elemento: ");
    scanf("%d", &quarto_elemento);

    int quinto_elemento = vetor[4];
    printf("\nDigite o quinto elemento: ");
    scanf("%d", &quinto_elemento);

    //Realiza a soma dos elementos
    int soma_elementos = (primeiro_elemento + segundo_elemento + terceiro_elemento +
    quarto_elemento + quinto_elemento);

    //Exibe os elementos, linha por linha
    printf("\nOs elementos sao: \n%d\n%d\n%d\n%d\n%d\n", 
    primeiro_elemento, segundo_elemento, terceiro_elemento,
    quarto_elemento, quinto_elemento);

    printf("\nSoma de todos os elementos = %d", soma_elementos);

    return 0;
    
}