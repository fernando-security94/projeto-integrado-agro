// ATIVIDADE PROPOSTA:

// Nesta atividade, deverá ser desenvolvido um programa em C 
// que utiliza a estrutura de repetição
// // “while” para executar uma tarefa 
// até que uma condição de parada seja satisfeita. 
// A atividade foca em como controlar loops baseados em condições de início, 
// garantindo a compreensão de como
// inicializar, executar e encerrar laços de repetição corretamente.
// Enunciado:

// Crie um programa em C que leia números inteiros do usuário
//  e calcule a soma de todos os números inseridos. 
//  O loop deve continuar até que o usuário insira o número zero, 
//  que será o valor sentinela para encerrar o programa.
// • Cenário: Imagine que você está desenvolvendo 
// uma ferramenta simples de cálculo, onde o usuário deseja 
// somar uma série de números inteiros 
// até decidir que não deseja inserir mais nenhum número. 
// A cada inserção, o programa deve somar os números já inseridos e permitir
// que o usuário continue até digitar o número 0 (zero), que encerra o programa e exibe o
// resultado final da soma.


#include <stdio.h>
#include <math.h>

int main(){
    int num, acumulador = 0; // zero atribuido para iniciar acumulador

    // iniciando programa para inserir dados
    printf("\nDigite um numero ou digite 0 para encerrar: ");
    scanf("%d", &num);

    // laço while que rodará em loop
    // enquanto o numero digitado pelo usuario
    // for diferente de zero
    while (num != 0)
    {   
        // vamos acumular o numero digitado pelo usuario
        // a cada iteração e soma-lo
        // a cada inserção de um novo numero
        acumulador += num;
        printf("\nSoma acumulada %d", acumulador);

        // exibir outra opçao para o usuario inserir numero
        // e atualizar o acumulador a cada iteração
        // ou encerrar.
        printf("\nDigite outro numero ou 0 para encerrar: ");
        scanf("%d", &num);

        
    }
    printf("\nPrograma encerrado!");

    return 0;

}