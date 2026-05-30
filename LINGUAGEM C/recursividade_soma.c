//Exemplos de funcoes recursivas
// Funcoes recursivas sao utilizadas para
// resolver problemas de instancias maiores ate
// instancias menores.

//Funcao recursiva de soma decrescente

#include <stdio.h>

int somar(int valor){
    if (valor != 0)  // critério de parada
    {
        printf("%d + ", valor);  // exibe numeros somados
        return valor + somar(valor - 1);
    }
    else
    {
        return valor;  // sera executado se valor = 0
    }
}

int main(){
    int numero, result;

    printf("\nDigite um numero inteiro positivo: ");
    scanf("%d", &numero);

    printf("\nNumeros somados: ");
    result = somar(numero);
    
    printf("\nSoma total = %d", result);

    return 0;
}