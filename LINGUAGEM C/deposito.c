// Sistema de deposito bancario

#include <stdio.h>
#include <math.h>

int main(){
    float soma = 0, valor;
    int opcao;

    // primeiro vai executar todos os comandos e depois
    // checar condicional
    do {
    printf("\nDigite a opcao desejada: \n");

    printf("\nOpcao 1 - Deposito\n");
    printf("\nOpcao 2 - Saque\n");
    printf("\nOpcao 3 - Saldo\n");
    printf("\nOpcao 4 - SAIR\n");
    scanf("%d", &opcao);
    
    // a função switch case funciona
    // parecido com else if
    switch (opcao)

    {
    // usamos um case para cada condicao
    // se o usuario selecionar a opcao x
    // executar tal comando;    
    case 1:
    printf("\nValor do deposito: $");
    scanf("%f", &valor);
        soma = soma + valor;
        printf("\nSaldo em conta: $%.2f\n", soma);
        break;
    
    case 2:
    printf("\nValor do saque: $");
    scanf("%f", &valor);
    soma = soma - valor;
    printf("\nSaldo em conta $%.2f\n", soma);
    break;

    case 3:
    printf("\nSaldo em conta: $%.2f\n", soma);
    break;
    
    default:
    if (opcao != 4) {
        printf("\nOpcao invalida");
        break;
        }
    }
}
// todos os comandos acima serão executados
// enquanto a opção for diferente de 4 
while (opcao != 4);
    printf("\nFim das operacoes.");
    
    return 0;
};