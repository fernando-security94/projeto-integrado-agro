#include <stdio.h>

int main(){

    int m, n, p, q, i, j, k;
    int soma = 0;

    printf("Digite as dimensoes da primeira matriz (m X n): \n");
    scanf("%d %d", &m, &n);

    printf("Digite as dimensoes da segunda matriz (p X q): \n");
    scanf("%d %d", &p, &q);

    // verificação se a multiplicacao e possivel
    if (n != p)
    {
        printf("A multiplicacao nao e possivel!\n");
        return 0; // encerrar se nao for possivel
    }

    // Declaracao e entrada dos elementos
    int matriz_1[m][n], matriz_2[p][q], result[m][q];

    printf("Digite os elementos da primeira matriz:\n");

    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            scanf("%d", &matriz_1[i][j]);
        }
        
    }

    printf("Digite os elementos da segunda matriz:\n");
    for (i = 0; i < p; i++)
    {
        for (j = 0; j < q; j++)
        {
            scanf("%d", &matriz_2[i][j]);
        }
        
    }

    // exibe a matriz_1
    printf("\nMatriz 1 exibida:\n");
    for (i = 0; i < m; i++) {
        for (j = 0; j < q; j++) {
            printf("%d\t", matriz_1[i][j]); // Tabulação para alinhar os números
        }
        printf("\n"); // Nova linha após cada linha da matriz
    }
    // exibe a matriz_2
    printf("\nMatriz 2 exibida:\n");
    for (i = 0; i < m; i++) {
        for (j = 0; j < q; j++) {
            printf("%d\t", matriz_2[i][j]); // Tabulação para alinhar os números
        }
        printf("\n"); // Nova linha após cada linha da matriz
    }


    // Inicializa a matriz resultado com zeros
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < q; j++)
           {
               result[i][j] = 0;
           }
    }

    // Calculo dos produtos das matrizes com exibicao dos valores
    printf("\nMultiplicacoes realizadas:\n");
    for (i = 0; i < m; i++) {
        for (j = 0; j < q; j++) {   
            for (k = 0; k < n; k++) {
                printf("(%d * %d)", matriz_1[i][k], matriz_2[k][j]);
                if (k < n - 1) {
                    printf(" + ");
                }
                result[i][j] += matriz_1[i][k] * matriz_2[k][j];
            }
            printf(" = %d\n", result[i][j]); // Mostra o resultado da soma
        }
    }
    
    printf("\nO produto das matrizes e:\n");
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < q; j++)
        {
            printf("%d\t", result[i][j]);
        }
        printf("\n");
    }
    return 0;
    
}


// correcoes chatGPT

// ## 🎯 **Resumo das correções**
// ✅ **1. Retirei o ponto e vírgula (`;`) no loop de leitura da segunda matriz.**  
// ✅ **2. Adicionei `return 0;` caso a multiplicação não seja possível.**  
// ✅ **3. Corrigi a inicialização de `result[i][j] = 0;` antes de acumular a soma.**  
// ✅ **4. Usei `\t` no `printf` para a exibição correta da matriz.**  
// ✅ **5. Ajustei a condição do loop interno para `k < n`, pois `n` define o número de colunas da primeira matriz.**  

// Agora o código está 100% funcional! 🚀🔥  
// Se precisar de mais alguma explicação, só avisar! 😊






// Ótimo que você percebeu o problema! Vamos analisar e corrigir os erros no seu código.

// ---

// ## 🛑 **Erros Identificados**
// ### 1️⃣ **Loop infinito na leitura da segunda matriz**
// Erro na linha:
// ```c
// for (i = 0; i < p; i++)
// {
//     for (j = 0; j < q; j++);  // <-- ERRO: ponto e vírgula aqui!
//     {
//         scanf("%d", &matriz_2[i][j]);
//     }
// }
// ```
// **O que acontece?**  
// - O **ponto e vírgula ( ; ) após o segundo `for`** encerra o loop antes de executar `scanf()`
// fazendo com que `j` mantenha um valor errado.  
// - Isso causa **comportamento inesperado ou um loop infinito**.

// ### ✅ **Correção:**
// Retire o `;` depois do `for`:
// ```c
// for (i = 0; i < p; i++)
// {
//     for (j = 0; j < q; j++)  // Agora sem o ponto e vírgula!
//     {
//         scanf("%d", &matriz_2[i][j]);
//     }
// }
// ```

// ---

// ### 2️⃣ **Erro na verificação da multiplicação**
// Você verifica se **a multiplicação é possível** com:
// ```c
// if (n != p)
// {
//     printf("A multiplicacao nao e possivel!\n");
// }
// ```
// Mas **depois continua executando o código!** Isso causa um **erro na alocação da matriz e possíveis loops infinitos**.

// ### ✅ **Correção:**
// Adicione um `return 0;` para encerrar o programa se a multiplicação não for possível:
// ```c
// if (n != p)
// {
//     printf("A multiplicacao nao e possivel!\n");
//     return 0;  // Sai do programa
// }
// ```

// ---

// ### 3️⃣ **Erro na alocação da matriz**
// O C **não permite** que arrays sejam declarados com tamanhos baseados 
//em variáveis antes do C99.
//Se seu compilador não suportar **VLA (Variable-Length Arrays)**
//será necessário usar **alocação dinâmica (`malloc`)**. 
//Caso contrário, continue com seu código.

// ---

// ### 4️⃣ **Erro na exibição da matriz final**
// No `printf`:
// ```c
// printf("%dt", result[i][j]);
// ```
// O `t` não é um caractere especial válido. O correto é `\t` para tabulação.

// ### ✅ **Correção:**
// ```c
// printf("%d\t", result[i][j]);
// ```

// ---

// ## 🔥 **Código Final Corrigido**
// ```c
// #include <stdio.h>

// int main()
// {
//     int m, n, p, q, i, j, k;
//     int soma = 0;

//     printf("Digite as dimensoes da primeira matriz (m X n): \n");
//     scanf("%d %d", &m, &n);

//     printf("Digite as dimensoes da segunda matriz (p X q): \n");
//     scanf("%d %d", &p, &q);

//     // Verifica se a multiplicação é possível
//     if (n != p)
//     {
//         printf("A multiplicacao nao e possivel!\n");
//         return 0;  // Sai do programa
//     }

//     // Declaração das matrizes
//     int matriz_1[m][n], matriz_2[p][q], result[m][q];

//     printf("Digite os elementos da primeira matriz:\n");
//     for (i = 0; i < m; i++)
//     {
//         for (j = 0; j < n; j++)
//         {
//             scanf("%d", &matriz_1[i][j]);
//         }
//     }

//     printf("Digite os elementos da segunda matriz:\n");
//     for (i = 0; i < p; i++)
//     {
//         for (j = 0; j < q; j++)  // Corrigido: sem o ponto e vírgula
//         {
//             scanf("%d", &matriz_2[i][j]);
//         }
//     }

//     // Inicializa a matriz resultado com zeros
//     for (i = 0; i < m; i++)
//     {
//         for (j = 0; j < q; j++)
//         {
//             result[i][j] = 0;
//         }
//     }

//     // Cálculo do produto das matrizes
//     for (i = 0; i < m; i++)
//     {
//         for (j = 0; j < q; j++)
//         {
//             soma = 0;
//             for (k = 0; k < n; k++)  // Corrigido: `k < n`, não `k < p`
//             {
//                 soma += matriz_1[i][k] * matriz_2[k][j];
//             }
//             result[i][j] = soma;
//         }
//     }

//     // Exibição da matriz resultante
//     printf("O produto das matrizes e:\n");
//     for (i = 0; i < m; i++)
//     {
//         for (j = 0; j < q; j++)
//         {
//             printf("%d\t", result[i][j]);  // Corrigido `\t`
//         }
//         printf("\n");
//     }

//     return 0;
// }




