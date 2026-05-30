// Operação com matriz 3x3, somando as diagonais.

#include <stdio.h>

int main(){
    int matriz[3][3];

    int i, j, sDiagPrinc = 0, SDiagSec = 0;

    //Leitura da matriz

    printf("Digite os elementos da matriz 3x3: \n");

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            scanf("%d", &matriz[i][j]);
        }
        
    }

    // Exibição da matriz
    printf("\nMatriz digitada:\n");
    for (i = 0; i < 3; i++) 
    {
        for (j = 0; j < 3; j++) 
            {
                printf("%d\t", matriz[i][j]); // Tabulação para melhor visualização
            }  
            printf("\n"); // Quebra de linha para manter o formato 3x3
    }

    //calculo da soma diagonal principal e secundaria
    for (i = 0; i < 3; i++)  // j-- omitido pq naturalmente ja reduz ate zero
    {
        sDiagPrinc += matriz[i][i];
        printf("\nValores somados: %d\n", matriz[i][i]);
        
        SDiagSec += matriz[i][2-i];  // foi feito -2 pq precisamos pegar a diagonal ao contrario
        printf("\nValores somados: %d\n", matriz[j][j]);     // se a matriz fosse 4, a diagonal seria -3.

        // printf("\nValores somados: %d\n", matriz[j][j]);
    }
    // exibição dos resultados
    printf("\nSoma diagonal principal: %d", sDiagPrinc);
    printf("\nSoma diagonal secundaria: %d\n", SDiagSec);

    return 0;
    
    
}

