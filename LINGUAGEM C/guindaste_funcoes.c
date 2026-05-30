//Exercicio para escolher o guindaste adequado
// de acordo com a capacidade de peso
// essa escolha sera feita atraves de funcoes e condicionais

#include <stdio.h>
#include <stdlib.h>

int calcularPeso(){
    float base, compri, altura = 0;

    printf("Valor da base: ");
    scanf("%f", &base);

    printf("Valor da altura: ");
    scanf("%f", &altura);

    printf("Valor do comprimento: ");
    scanf("%f", &compri);
    
    return (int)(base * compri * altura * 25); //cast feito (int) para garantir retorno int

}

int main(){
    float peso;

    peso = calcularPeso();

    if (peso <= 500)
    {   
        printf("\nPeso total: %.2f\n", peso);
        printf("\nO guindaste modelo G1 deve ser usado!");
    }
    else if (peso > 1500)
    {   
        printf("Peso total: %.2f\n", peso);
        printf("O guindaste modelo G3 deve ser usado!");
    }
    else
    {
        printf("Peso total: %.2f\n");
        printf("O guindaste modelo G2 deve ser usado!");
    }
    
    return 0;
}