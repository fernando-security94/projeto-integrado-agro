#include <stdio.h>

int main(){
    // programa que exibe figura geometrica

    int linhas, espacos, asteriscos;
    
    printf("\nDigite o numero de linhas da figura: ");
    scanf("%d", &linhas);

    for (int i = 1; i <= linhas - i; i++)
    {
        for (espacos = 1; espacos <= linhas - i; espacos++)
        {
            printf(" ");
        }
        for (asteriscos= 1; asteriscos <=2 * i - 1; asteriscos++)
        {
            printf("*");
        }

        printf("\n");
    }

    return 0;
    
}

//Este programa solicita ao usuário 
//o número de linhas desejado para o triângulo e, em seguida, 
//usa dois loops for para imprimir o triângulo na tela. 
//O primeiro for interno gerencia a quantidade de espaços em branco
// que devem ser impressos, ao passo que o segundo imprime os asterisco.