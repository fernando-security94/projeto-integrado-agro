// Utilizacao de ponteiros em funcoes

#include <stdio.h>
#include <stdlib.h>

//Funcao com ponteiro 
//que gera numeros aleatorios entre 0-99
int* gerarRandomico(){
    static int r[10];
    int a;

    for (a = 0; a < 10; a++)
    {
        r[a] = rand() % 100; // limitar range 0-99
        
        printf("r[%d] = %d\n", a, r[a]);
    }

    return r;
    
}

int main(){
    int* ponteiro;
    int i;

    ponteiro = gerarRandomico();

    for (i = 0; i < 10; i++)
    {   
        // exibe endereco de memoria
        printf("\nEndereco de memoria:");
        printf("\n[%d] = %p\n", i, *(ponteiro + i));
    }
    
    return 0;
}