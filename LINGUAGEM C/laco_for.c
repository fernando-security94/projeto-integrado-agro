#include <stdio.h>
#include <string.h>
#include <math.h>

int main(){
    int i, j;

    for (i = 0, j = 100; i <= j; i++, j--)
    {
        printf("\ni = %d e j = %d\n", i, j);
    }
    

    return 0;

// criando algoritmo que calcula expoentes, 
// sem importar biblioteca.

    int x, z;
    long int resultado = 1;

    printf("\nDigite o valor de X: ");
    scanf("%d", &x);

    printf("\nDigite o valor de Z: ");
    scanf("%d", &z);

    for (int i = 0; i < z; i++)
    {   // enquanto i for menor que Z
        // vou multiplicar o resultado por x,
        // add 1 a cada laço
        resultado = resultado * x;
    }
    printf("%d elevado a %d = %d\n", x, z, resultado);

    if (z = 0)
    {   resultado = 1;
        printf("\n%d elevado a %d = ", x, z, resultado);
    }


    
    return 0;
}