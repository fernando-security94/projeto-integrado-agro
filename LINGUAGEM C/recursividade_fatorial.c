//Calculo fatorial com funcao recursiva

#include <stdio.h>

int fatorial(int valor){
    if (valor > 0)
    {
        printf("%d * ", valor);
        return valor * fatorial(valor - 1);
    }
    else
    {
        return 1;
    }
    
}

int main(){
    int numero, result;

    printf("Digite um numero inteiro positivo: ");
    scanf("%d", &numero);

    if (numero < 0)
    {
        printf("\nNumeros negativos nao sao permitidos\n");
    }
    else
    {
        result = fatorial(numero);
        printf("\nFatorial de %d = %d", numero, result);
    }

    return 0;
    
}