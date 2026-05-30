// Sequencia de Fibonacci em C.
// A sequencia de Fibonacci sempre terá os dois primeiros numeros = 0 e 1.
// Os numeros seguintes são resultado da soma com o número interior. 
// Portanto: 0 1;  0 + 1 = 0 1 1; 0 + 1 + 1 = 0 1 1 2 e assim
// sucessivamente.


#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int a, b, acumulador, i, numero;
    // os dois primeiros numeros sempre serao
    // 0 e 1
    a = 0;
    b = 1;

    printf("\nDigite um numero: ");
    scanf("%d", &numero);

    printf("\nSequencia de Fibonacci: \n");
    printf("\n%d ", a);

    for (i = 0; i < numero; i++)
    {
        acumulador = a + b;
        a = b;
        b = acumulador;

        printf("%d ", acumulador);
    }
    
    return 0;

}