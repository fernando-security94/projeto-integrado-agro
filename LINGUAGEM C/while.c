#include <stdio.h>
#include <math.h>

int main(){

    // tabuada com while
    int multiplicator = 0, result, num;
    printf("\nTabuada de qual numero? ");
    scanf("%d", &num);

    while (multiplicator <= 10)
    {
        result = num * multiplicator;
        printf("%d\n", result);

        multiplicator = multiplicator + 1; 
        
    }
    printf("\n");
    
    float metragem1 = 0, metragem2 = 0, resultado = 0;
    int resposta;

    do
    {
        printf("\nCalculo de metros quadrados.");

        printf("\nTire a primeira medida: ");
        scanf("%f", &metragem1);

        printf("\nTire a segunda medida: ");
        scanf("%f", &metragem2);

        resultado = (metragem1 * metragem2);
        printf("\nO terreno tem %.f metros quadrados \n", resultado);

        printf("\nDigite (1) para continuar ou (2) para sair \n");
        scanf("%d", &resposta);


    } while (resposta == 1); // condição de saida
    

    return 0;
}

