// sistema de estoque de livros

#include <stdio.h>
#include <string.h>

#define NUM_LIVROS 4

struct Livros{
    char titulo[100];
    char autor[50];
    char ISBN[13];
    int anoPublicado;
    int estoque;
};

int main(){
    struct Livros livros[NUM_LIVROS]
    = {
        {
            "Memorias de um Futuro Esquecido",
            "Machado de Assis",
            "1231231231239", 1899, 10
        },
        {
            "Biblia Sagrada", "King James",
            "1234567891011", 1400, 7
        },

        {
            "O silencio dos inocentes Gritando",
            "Franz Kafta", "4564564564569", 
            1899, 5

        },

        {
            "A menina que roubava livros os devolvia com juros",
            "Dan Brownie", "7897897897899", 1949, 8
        }
    };

    //realizar busca por autor
    char autorProcurado[50];

    printf("\nDigite o autor desejado: ");
//    while (getchar() != '\n'); // limpa o buffer de entrada
    fgets(autorProcurado, 50, stdin);  // sempre insere \n, conflitando com strcmp
    
    autorProcurado[strcspn(autorProcurado, "\n")] = 0; // remove o \n ao final da str

    printf("Livros por %s:\n", autorProcurado);

    for (int  i = 0; i < NUM_LIVROS; i++)
    {
        if (strcmp(livros[i].autor, autorProcurado) == 0)
        {
            printf("Titulo: %s\n",  livros[i].titulo);
            printf("ISBN: %s\n", livros[i].ISBN);
            printf("Ano publicado: %d\n", livros[i].anoPublicado);
            printf("Estoque disponivel: %d\n", livros[i].estoque);

            printf("\n");
        }
        
    }

    // verificar disponinibilidade de um livro
    char ISBNProcurado[14];

    printf("Digite o ISBN do livro desejado para disponibilidade: ");
//    while(getchar()!= '\n');
    fgets(ISBNProcurado, 14, stdin);

    ISBNProcurado[strcspn(ISBNProcurado, "\n")] = 0; // remove \n final da string

    for (int i = 0; i < NUM_LIVROS; i++)
    {
        if (strcmp(livros[i].ISBN, ISBNProcurado) == 0)
        {
            printf("O livro '%s' esta disponivel em estoque: %d", 
                livros[i].titulo, livros[i].estoque);

            break;
        }
        
    }

    return 0;
}
