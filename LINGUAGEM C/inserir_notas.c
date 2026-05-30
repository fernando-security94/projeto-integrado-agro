#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int avalia, contador = 0, soma = 0;
    char letra;
    float media;

    do {
        printf("\nDigite uma nota: ");
        scanf("%d", &avalia);
        fflush(stdin);  // limpa o buffer de entrada 

        contador++;
        soma = soma + avalia;
        printf("\n", avalia);

        printf("Digite qualquer letra ou 's' para encerrar\n");
    }
    while ((letra = getchar()) !='s');
    {
        printf("\nQuantidade de avaliacoes = %d, e soma das notas = %d. \n", contador, soma);
        media = soma / contador;
        system("PAUSE");
    }
    
return 0;
}