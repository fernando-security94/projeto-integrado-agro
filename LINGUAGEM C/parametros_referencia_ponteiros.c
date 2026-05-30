// Passagem de parametros por referencia com ponteiros
#include <stdio.h>

void dobrar(int *numero){
    *numero *= 2;
}

int main(){
    int valor = 5;

    printf("\nValor antes da chamada: %d", valor);

    dobrar(&valor);
    
    printf("\nValor depois da chamada: %d", valor);

    return 0;
}
