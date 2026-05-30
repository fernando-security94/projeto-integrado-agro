// Formatar CPF em um formato sem pontos e traço.

#include <stdio.h>
#include <stdlib.h>

int main(){
    // Vetor CPF com pontos e traço
    char cpf1[15];

    // Vetor CPF formatado, inicializado vazio
    char cpf2[12] = "";

    int i = 0, n = 0;

    printf("\nDigite seu CPF com pontos e tracos: \n");
    scanf("%s", &cpf1);

    // Laço para percorrer vetor cpf1
    // e remover pontos e traços

    for (i = 0; i < 14; i++)
    {
        if (cpf1[i] =='.' || cpf1[i] =='-')
        {
            continue;  // ignora pontos e traços
        }
        else
        // armazena apenas digitos em cpf2
            cpf2[n] = cpf1[i];
            n++; // controla o tamanho de cpf2
    }
    // Imprime CPF formatado
    printf("\n\nCPF formatado: %s", cpf2);
return 0;
}
