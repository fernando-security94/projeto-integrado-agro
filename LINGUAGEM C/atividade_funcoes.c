// Criar um programa em C que realize o calculo 
// do salario bruto, desconto e salario liquido,
// baseado no valor/hora e nas horas trabalhadas;
// Modularizar três funcoes para os calculos citados;
// Solicitar entrada de valores do usuario
// Exibir todos os resultados.

#include <stdio.h>

//variaveis globais que serao utilizadas pelas funcoes
int horas_trabalhadas;
float valor_hora, salario_bruto, desconto, salario_liquido;

// funcao que calcula salario bruto
float calcular_bruto(){
    salario_bruto = valor_hora * horas_trabalhadas;
    return salario_bruto;
}

// funcao que calcula desconto de 9% em cima do salario bruto
float calcular_desconto(){
    desconto = salario_bruto * 0.09;
    return desconto;
}

// funcao que calcula salario liquido
float calcular_liquido(){
    return salario_bruto - desconto;
}

int main(){

    // atribuicao de valores as variaveis globais
    printf("\nDigite o valor/hora: $");
    scanf("%f", &valor_hora);

    printf("\nDigite as horas trabalhadas: ");
    scanf("%d", &horas_trabalhadas);

    // chamada das funcoes
    calcular_bruto();    
    printf("\nSalario bruto = $%.2f\n", salario_bruto);

    calcular_desconto();
    printf("\nDesconto total: $%2.f\n", desconto);

    salario_liquido = calcular_liquido();
    printf("\nSalario liquido: $%.2f\n", salario_liquido);

    return 0;
}