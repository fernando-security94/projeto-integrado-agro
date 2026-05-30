// exemplos de structs

#include <stdio.h>
#include <string.h>

struct Cadastro
{
    char cpf[12];
    char nome[30];
    int idade;
    char rua[50];
    int numero;
}cliente_1, cliente_2;  // Os membros de cadastro estarão nas duas variaveis

int main(){
    strcpy(cliente_1.cpf, "12345678990");
    strcpy(cliente_1.nome, "Fernando");
    strcpy(cliente_1.rua, "Rua abc");
    cliente_1.idade = 31;
    cliente_1.numero = 100;

    strcpy(cliente_2.cpf, "00011122234");
    strcpy(cliente_2.nome, "Poliane");
    strcpy(cliente_2.rua, "Rua espanha");
    cliente_2.idade = 45;
    cliente_2.numero = 20;

    printf("\nNomes dos clientes: %s, %s", cliente_1.nome, cliente_2.nome);
    printf("\nIdades do clientes: %d, %d", cliente_1.idade, cliente_2.idade);
    printf("\nCPF dos clientes: %s, %s", cliente_1.cpf, cliente_2.cpf);
    printf("\nEnderecos dos clientes: %s n %d, %s n %d ", 
    cliente_1.rua, cliente_1.numero, cliente_2.rua, cliente_2.numero);

    return 0;
    
}
