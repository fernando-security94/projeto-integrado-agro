// Passagem de parametros por referencia com vetores

#include <stdio.h>

void inserir(int a[]){
    int i = 0; 
    for (i = 0; i < 3; i++)
    {
        printf("Digite os valores desejados[%d]: ", i);
        scanf("%d", &a[i]);
    }
    
}

void imprimir(const int b[]){
    int i = 0;
    for (i = 0; i < 3; i++)
    {
        printf("\nNumeros[%d] = %d", i, 2 * b[i]);
    }
    
}

// funcao que soma os numeros dobrados
int somaDobrado(const int b[]){
    int i, soma = 0;
    for (i = 0; i < 3; i++)
    {
        soma += 2 * b[i];
    }
    return soma;
    
}

int main(){
    int numeros[3];
    int soma;
    printf("\nPreenchendo o vetor...\n");

    //funcao de inserir numeros
    inserir(numeros);

    printf("\nDobro dos valores informados: ");

    // funcao que imprime os valores dobrados
    imprimir(numeros);
    printf("\n");

    //funcao que soma os dobrados
    soma = somaDobrado(numeros);
    printf("Soma dos valores dobrados: %d\n", soma);


    return 0;
}