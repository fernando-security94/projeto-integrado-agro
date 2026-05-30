#include <stdio.h>
#include <math.h>


int fatorial(int n){
    int result = 1;

    if (n == 0)
    {
        return 1;
    }
    else
    {
        for (int i = n; i > 1; i--)
        {
            result = result * i;
        }
        
    }
    return result;
    
}

int main(){
    int numero, result;

    printf("Digite um numero inteiro positivo: ");
    scanf("%d", &numero);

    if (numero < 0)
    {
        printf("Numeros negativos nao sao permitidos!");
    }
    else
    {
        printf("Fatorial de %d: %d",numero, fatorial(numero));
    }
    
    return 0;
}