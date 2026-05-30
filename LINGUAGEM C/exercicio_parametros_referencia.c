// A seguir, seguem alguns detalhes da implementação.
// A função calcularPrecoTotal é usada para calcular o preço total da compra, 
// considerando os preços unitários e as quantidades de cada item.
// Os vetores precoUnitario e a quantidade são passados por referência para a 
// função para garantir a atualização correta das variáveis.
// O programa solicita ao usuário o número de itens comprados e depois 
// solicita o preço unitário e a quantidade de cada item. 
// Em seguida, ele chama a função calcularPrecoTotal para calcular o 
// preço total da compra e, em seguida, exibe o preço total na saída.
// A passagem de parâmetros por referência neste caso torna 
// o programa mais eficiente, pois permite que as variáveis 
// sejam atualizadas diretamente na função chamadora sem a necessidade 
// de retornar valores, além de possibilitar a passagem de vetores e matrizes





#include <stdio.h>

void calcularPrecoTotal(float precoUnitario[],
int quantidade[], int numItens, float *precoTotal){

    *precoTotal = 0;

    for (int i = 0; i < numItens; i++)
    {
        *precoTotal += precoUnitario[i] * quantidade[i];
    }
    
}

int main(){
    int numItens;

    printf("Digite o numero de itens comprados: ");
    scanf("%d", &numItens);

    float precoUnitario[numItens];
    int quantidade[numItens];
    float precoTotal;

    // Entrada dos precos unitarios e quantiade
    // de cada item
    for (int i = 0; i < numItens; i++)
    {
        printf("Digite o preco unitario %d: ", i + 1);
        scanf("%f", &precoUnitario[i]);

        printf("Digite a quantiade do item %d: ", i + 1);
        scanf("%d", &quantidade[i]);
    }
    
    // chamada da funcao para calcular preco

    calcularPrecoTotal(precoUnitario, quantidade, 
        numItens, &precoTotal);
    
    // exibindo o preco total da compra
    printf("\nPreco total da compra: R$%.2f\n\n", precoTotal);
    
    return 0;
}

