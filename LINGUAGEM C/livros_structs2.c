// sistema de estoque de livros com menu de opcoes
// adição e exclusao de livros

#include <stdio.h>
#include <string.h>

#define NUM_LIVROS 4

struct Livros {
    char titulo[100];
    char autor[50];
    char ISBN[14]; // 13 caracteres + '\0'
    int anoPublicado;
    int estoque;
};

// menu de seleção
void buscarLivro(struct Livros livros[], int totalLivros) {
    int opcao;
    printf("\nBuscar livro por:\n1 - Autor\n2 - Titulo\nEscolha: ");
    scanf("%d", &opcao);
    while (getchar() != '\n'); // Limpa buffer

    // execucao do menu de selecao com switch-case
    switch (opcao) {
        case 1: { // Busca por autor
            char autorProcurado[50];
            printf("\nDigite o autor desejado: ");
            fgets(autorProcurado, 50, stdin);
            autorProcurado[strcspn(autorProcurado, "\n")] = '\0';

            printf("\nLivros por %s:\n", autorProcurado);
            int encontrou = 0;
            for (int i = 0; i < totalLivros; i++) {
                if (strcmp(livros[i].autor, autorProcurado) == 0) {
                    printf("Titulo: %s\nISBN: %s\nAno: %d\nEstoque: %d\n\n",
                           livros[i].titulo, livros[i].ISBN, livros[i].anoPublicado, livros[i].estoque);
                    encontrou = 1;
                }
            }
            if (!encontrou) printf("Nenhum livro encontrado.\n");
            break;
        }


        case 2: { // Busca por ISBN
            char TituloProcurado[100];
            printf("\nDigite o titulo do livro: ");
            fgets(TituloProcurado, 100, stdin);
            TituloProcurado[strcspn(TituloProcurado, "\n")] = '\0';

            int encontrou = 0;
            for (int i = 0; i < totalLivros; i++) {
                if (strcmp(livros[i].titulo, TituloProcurado) == 0) {
                    printf("\nO livro \"%s\" esta disponivel: %d unidades\n",
                           livros[i].titulo, livros[i].estoque);
                    encontrou = 1;
                    break;
                }
            }
            if (!encontrou) printf("\nLivro nao encontrado.\n");
            break;
        }
        default:
            printf("\nOpcao invalida.\n");
    }
}


// manipulaçao de estoque
void alterarEstoque(struct Livros livros[], int totalLivros) {
    char titulo[100];
    printf("\nDigite o titulo do livro para modificar o estoque: ");
    fgets(titulo, 100, stdin);
    titulo[strcspn(titulo, "\n")] = '\0';

    // laço for para percorrer total de livros
    for (int i = 0; i < totalLivros; i++) {
        if (strcmp(livros[i].titulo, titulo) == 0) {
            int opcao, quantidade;
            printf("\n1 - Adicionar estoque\n2 - Remover estoque\n3 - Checar estoque:\nEscolha: ");
            scanf("%d", &opcao);
            while (getchar() != '\n'); // Limpa buffer

            // quantidade que será adicionada ou removida
            printf("Quantidade: ");
            scanf("%d", &quantidade);
            while (getchar() != '\n');

            // condicional para adicionar ou remover do estoque
            if (opcao == 1) {
                livros[i].estoque += quantidade;
                printf("\nEstoque atualizado: %d unidades.\n", livros[i].estoque);
            } else if (opcao == 2) {
                // se numero de livros para remover for maior que a qtd de estoque
                if (quantidade > livros[i].estoque) {
                    printf("\nErro: estoque insuficiente!\n");
                }
                
                else 
                {
                    livros[i].estoque -= quantidade;
                    printf("\nEstoque atualizado: %d unidades.\n", livros[i].estoque);
                }
            } else {
                printf("\nOpcao invalida.\n");
            }
            return;
        }
    }
    printf("\nLivro nao encontrado.\n");
}

int main() {
    struct Livros livros[NUM_LIVROS] = {
        {"Memorias de um Futuro Esquecido", "Machado de Assis", "1231231231239", 1899, 10},
        {"O silencio dos inocentes Gritando", "Franz Kafta", "4564564564569", 1899, 5},
        {"A menina que roubava livros os devolvia com juros", "Dan Brownie", "7897897897899", 1949, 8},
        {"Biblia Sagrada", "King James", "1112223334449", 1400, 10}
    };

    int opcao;

    // O programa continuará rodando enquanto a opcao digitada pelo usuario for
    // for diferente de 3.
    do {
        printf("\n1 - Buscar Livro\n2 - Modificar Estoque\n3 - Sair\nEscolha: ");
        scanf("%d", &opcao);
        while (getchar() != '\n');

        switch (opcao) {
            case 1:
                buscarLivro(livros, NUM_LIVROS);
                break;
            case 2:
                alterarEstoque(livros, NUM_LIVROS);
                break;
            case 3:
                printf("\nSaindo...\n");
                break;
            default:
                printf("\nOpcao invalida!\n");
        }
    } while (opcao != 3);

    return 0;
}
