#include <stdio.h>
#include <string.h>
#include <math.h>

int main(){
    int numeros[5] = {100, 20, 30, 40, 50};

    int *ponteiro = &numeros[0];  // usar & quando apontar explicitamente ao indice?

    //Acessando primeiro elemento
    int primeiro_elemento = *ponteiro;

    //Acessando segundo elemento
    int segundo_elemento = *(ponteiro + 1);

    //Acessando terceiro elemento
    int terceiro_elemento = *(ponteiro + 2);
    
    //Acessando quarto elemento
    int quarto_elemento = *(ponteiro + 3);

    //Acessando quinto elemento
    int quinto_elemento = *(ponteiro + 4);
    

    printf("\nEndereco do ponteiro: %p", &ponteiro);
    printf("\nConteudo do ponteiro: %p", ponteiro);  // pode ser considerado endereco da variavel
    printf("\nConteudo da variavel pelo ponteiro: %d, sem indice, apontara sempre para o primeiro valor",
     *ponteiro);  // sem o indice, imprime primeiro valor

    // para imprimir indice nao se usa *
    printf("\nConteudo da variavel pelo ponteiro no indice 2: %d", ponteiro[2]);

    printf("\nConteudo da variavel pelo ponteiro no indice 4: %d", quinto_elemento);



    return 0;
}