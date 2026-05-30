// calculo fatorial hard coded

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int numero;
    // unsigned long long armazena numeros grandes
    unsigned long long fatorial = 1;

    printf("Digite um numero inteiro positivo: ");
    scanf("%d", &numero);

    // verificacao para numeros negativos
    if (numero < 0)
    {
        printf("\nO fatorial nao esta definido para numeros negativos.");
    }
    else
    {
        for (int i = 1; i <= numero; i++)
        {
            fatorial *= i;
        }

        printf("Fatorial %d = %llu\n", numero, fatorial);
        
    }



    return 0;
}


// Neste programa, o usuário insere um número inteiro positivo "numero", 
// que utiliza um laço "for" para calcular o fatorial de "numero". 
// O resultado é armazenado na variável "fatorial," que é inicializada como 1 
// para tratar o caso de 0! = 1. Por exemplo, se o usuário insere 0 (zero), 
// o loop “for”não é executado, e a variável “fatorial” permanece valendo 1. 
// Caso “numero” seja maior ou igual a 1,
// o laço percorre todos os números de 1 a "numero" 
// e multiplica-os para calcular o fatorial. O resultado é impresso no final.