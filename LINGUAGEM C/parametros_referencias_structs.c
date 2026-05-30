//Passagem de parametros por referencias com structs

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Pessoa
{
    char nome[50];
    int idade;
};

void modificarPessoa(struct Pessoa *p)
{
    p -> idade = 30;
};

int main(){
    struct Pessoa pessoa1;
    strcpy(pessoa1.nome, "Joao");
    pessoa1.idade = 25;

    modificarPessoa(&pessoa1);

    printf("Nome: %s\n", pessoa1.nome);
    printf("Idade: %d\n", pessoa1.idade);

    return 0;

}