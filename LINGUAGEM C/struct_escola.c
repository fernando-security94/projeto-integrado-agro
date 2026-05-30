// solucao chatgpt
#include <stdio.h>
#include <string.h>

struct Aluno
{
    char nome[50];
    int matricula;
    float notas[2];  // 2 disciplinas
};

struct Turma
{
    int numeroTurma;
    struct Aluno alunos[30]; // até 30 alunos por turma
    int totalAlunos;
};

int main(){
    struct Aluno alunos[5];
    struct Turma turmas[10];  // até 10 turmas na escola
    int opcao;

    // Cadastrar alunos
    strcpy(alunos[0].nome, "Joao");
    alunos[0].matricula = 1000;
    alunos[0].notas[0] = 8.5;
    alunos[0].notas[1] = 7.0;

    strcpy(alunos[1].nome, "Maria");
    alunos[1].matricula = 1001;
    alunos[1].notas[0] = 7.5;
    alunos[1].notas[1] = 8.0;

    strcpy(alunos[2].nome, "Pedro");
    alunos[2].matricula = 1002;
    alunos[2].notas[0] = 9.0;
    alunos[2].notas[1] = 9.0;

    strcpy(alunos[3].nome, "Ana");
    alunos[3].matricula = 1003;
    alunos[3].notas[0] = 7.0;
    alunos[3].notas[1] = 7.5;  // Corrigido índice de notas

    strcpy(alunos[4].nome, "Carlos");
    alunos[4].matricula = 1004;
    alunos[4].notas[0] = 8.0;
    alunos[4].notas[1] = 8.5;

    // Inicializa duas turmas
    turmas[0].totalAlunos = 0;
    turmas[0].numeroTurma = 5000;

    turmas[1].totalAlunos = 0;
    turmas[1].numeroTurma = 6000;

    int a, t;
    float mediaTurma = 0.0;

    do
    {
        printf("\n1- Cadastrar aluno na turma\n");
        printf("2- Lancar nota de aluno\n");
        printf("3- Media da turma\n");
        printf("4- Relatorio da turma\n");
        printf("5- Encerrar\n");
        printf("Opcao: ");
        scanf("%d", &opcao);

        switch (opcao)
        {
        case 1:
            printf("Escolha o aluno (0-4): ");
            scanf("%d", &a);

            if (a < 0 || a >= 5) {
                printf("Aluno invalido!\n");
                break;
            }

            printf("Escolha a turma (5000 ou 6000): ");
            scanf("%d", &t);

            int turmaIndex = -1;
            for (int i = 0; i < 2; i++) {
                if (turmas[i].numeroTurma == t) {
                    turmaIndex = i;
                    break;
                }
            }

            if (turmaIndex == -1) {
                printf("Turma não encontrada!\n");
                break;
            }

            if (turmas[turmaIndex].totalAlunos < 30)
            {
                turmas[turmaIndex].alunos[turmas[turmaIndex].totalAlunos] = alunos[a];
                turmas[turmaIndex].totalAlunos++;
                printf("Aluno adicionado com sucesso!\n");
            }
            else
            {
                printf("A turma esta cheia. Não é possível adicionar mais alunos.\n");
            }
            break;

        case 2:
            printf("Escolha o aluno (0-4): ");
            scanf("%d", &a);
            
            if (a < 0 || a >= 5) {
                printf("Aluno invalido!\n");
                break;
            }

            for (int i = 0; i < 2; i++)
            {
                printf("Nota %d: ", i + 1);
                scanf("%f", &alunos[a].notas[i]);
            }
            break;

        case 3:
            printf("Escolha a turma (5000 ou 6000): ");
            scanf("%d", &t);

            turmaIndex = -1;
            for (int i = 0; i < 2; i++) {
                if (turmas[i].numeroTurma == t) {
                    turmaIndex = i;
                    break;
                }
            }

            if (turmaIndex == -1) {
                printf("Turma nao encontrada!\n");
                break;
            }

            mediaTurma = 0.0;

            for (int i = 0; i < turmas[turmaIndex].totalAlunos; i++)
            {
                float somaNotas = 0.0;

                for (int j = 0; j < 2; j++) // Corrigido j < 2
                {
                    somaNotas += turmas[turmaIndex].alunos[i].notas[j];
                }
                mediaTurma += somaNotas / 2;
            }

            printf("\nMedia da turma: %.2f\n", turmas[turmaIndex].totalAlunos > 0 ? mediaTurma / turmas[turmaIndex].totalAlunos : 0);
            break;

        case 4:
            printf("Escolha a turma (5000 ou 6000): ");
            scanf("%d", &t);

            turmaIndex = -1;
            for (int i = 0; i < 2; i++) {
                if (turmas[i].numeroTurma == t) {
                    turmaIndex = i;
                    break;
                }
            }

            if (turmaIndex == -1) {
                printf("Turma não encontrada!\n");
                break;
            }

            printf("\nTurma %d\n", turmas[turmaIndex].numeroTurma);
            for (int i = 0; i < turmas[turmaIndex].totalAlunos; i++)
            {
                printf("Aluno: %s\n", turmas[turmaIndex].alunos[i].nome);
                printf("Matricula: %d\n", turmas[turmaIndex].alunos[i].matricula);
                printf("Notas: %.2f e  %.2f\n", turmas[turmaIndex].alunos[i].notas[0], turmas[turmaIndex].alunos[i].notas[1]);
            }
            break;

        default:
            printf("Programa encerrado!\n");
            break;
        }

    } while (opcao != 5);

    return 0;
}

// A sugestão de solução dada simula um sistema de gerenciamento de turmas e alunos em uma escola.

// Duas estruturas são definidas: struct Aluno e struct Turma, 
// que representam respectivamente os dados de um aluno e de uma turma. 
// A struct Turma possui como membro um vetor ds estrutura Aluno, 
// representando os alunos que pertencem à turma.
// O usuário tem acesso a um menu de opções que inclui:
// Adicionar um aluno a uma turma.
// Lançar notas de um aluno.
// Calcular a média da turma.
// Gerar um relatório da turma.
// Encerrar o programa.
// As funcionalidades do menu são implementadas utilizando um loop do-while e um switch-case. O programa imprime na tela as opções do menu e solicita a entrada do usuário para realizar as operações desejadas.
// A lógica de cada funcionalidade esta associada a um “case”.



























































































































// //  Sistema de gerenciamento de notas para
// // automatizar informações sobre turmas e alunos
// // O sistema permite cadastrar alunos, lançar notas, calcular medias
// // e gerar relatorios para cada turma.

// #include <stdio.h>
// #include <string.h>

// struct Aluno
// {
//     char nome[50];
//     int matricula;
//     float notas[2];  // 2 disciplinas
// };

// struct Turma
// {
//     int numeroTurma;
//     struct Aluno alunos[30]; // ate 30 alunos por turma
//     int totalAlunos;
// };

// int main(){
//     struct Aluno alunos[5];
//     struct Turma turmas[10];  // ate 10 turmas na escola

//     int opcao;

//     //Cadastrar alunos

//     strcpy(alunos[0].nome, "Joao");
//     alunos[0].matricula = 1000;
//     alunos[0].notas[0] = 8.5;
//     alunos[0].notas[1] = 7.0;

//     strcpy(alunos[1].nome, "Maria");
//     alunos[1].matricula = 1001;
//     alunos[1].notas[0]= 7.5;
//     alunos[1].notas[1] = 8;

//     strcpy(alunos[2].nome, "Pedro");
//     alunos[2].matricula = 1002;
//     alunos[2].notas[0] = 9.0;
//     alunos[2].notas[1] = 9.0;

//     strcpy(alunos[3].nome, "Ana");
//     alunos[3].matricula = 1003;
//     alunos[3].notas[0] = 7.0;
//     alunos[3].notas[1] = 7.5;

//     strcpy(alunos[4].nome, "Carlos");
//     alunos[4].matricula = 1004;
//     alunos[4].notas[0] = 8.0;
//     alunos[4].notas[1] = 8.5;

//     //Inicializa duas turmas
//     turmas[0].totalAlunos = 0;
//     turmas[0].numeroTurma = 5000;

//     turmas[1].totalAlunos = 0;
//     turmas[1].numeroTurma = 6000;

    
//     // turmas[2].totalAlunos = 0;
//     // turmas[2].numeroTurma = 7000;

    
//     // turmas[3].totalAlunos = 0;
//     // turmas[3].numeroTurma = 6000

//     int a, t;
//     float mediaTurma = 0.0;

//     do
//     {
//         printf("\n1- Cadastrar aluno na turma\n");
//         printf("\n2- Lancar nota de aluno\n");
//         printf("\n3- Media da turma\n");
//         printf("\n4- Relatorio da turma\n");
//         printf("\n5- Encerrar\n");
//         printf("Opcao: ");
//         scanf("%d", &opcao);

//         switch (opcao)
//         {
//         case 1:
//             printf("Escolha o aluno (0-4): ");
//             scanf("%d", &a);

//             //Checa se aluno é valido
//             if (a < 0 || a >= 5)
//             {
//                 printf("Aluno inválido!\n");
//                 break;
//             }
            

//             printf("Escolha a turma (5000 ou 6000): ");
//             scanf("%d", &t);

//             int turmaIndice = -1;
//             for (int i = 0; i < 2; i++)
//             {
//                 if (turmas[i].numeroTurma == t)
//                 {
//                     turmaIndice = i;
//                 }  
//             }

//             if (turmaIndice == -1)
//             {
//                 printf("Turma nao encontrada");
//                 break;
//             }

//             if (turmas[turmaIndice].totalAlunos < 30)
//             {
//                 printf("Aluno adicionado!\n");
//             }

//             else
//             {
//                 printf("A turma esta cheia. Nao e possivel adicionar mais alunos\n");
//             }
//             break;

//             case 2:
//             printf("Escolha o aluno (0-4): ");
//             scanf("%d", &a);

//             if (a < 0 || a >= 5)
//             {
//                 printf("Aluno invalido\n");
//                 break;
//             }
            
//             for (int i = 0; i < 2; i++)
//             {
//                 printf("Nota %d: ", i+1);
//                 scanf("%f", &alunos[a].notas[i]);
//             }
//             break;
            
//             case 3:
//             printf("Escolha a turma (5000 ou 6000): ");
//             scanf("%d", &t);

//             turmaIndice = -1;
//             for (int i = 0; i < 2; i++)
//             {
//                 if (turmas[i].numeroTurma == t)
//                 {
//                     turmaIndice = i;
//                     break;
//                 }  
//             }
//             if (turmaIndice == -1)
//             {
//                 printf("Turma nao encontrada\n");
//             }

//             mediaTurma = 0.0;

//             for (int i = 0; i < turmas[turmaIndice].totalAlunos; i++)
//             {
//                 float somaNotas = 0.0;

//                 for (int j = 0; j < 2; j++)
//                 {
//                     somaNotas += turmas[turmaIndice].alunos[i].notas[j];
//                 }
//                 mediaTurma += somaNotas / 2;    
//             }

//             printf("\nMedia: %.2f", mediaTurma / turmas[turmaIndice].totalAlunos > 0 ? 
//                 mediaTurma/ turmas[turmaIndice].totalAlunos: 0);

//             break;

//             case 4:
//             printf("Escolha a turma (5000 ou 6000): ");
//             scanf("%d", &t);

//             turmaIndice = -1;
//             for (int i = 0; i < 2; i++)
//             {
//                 if (turmas[i].numeroTurma == t)
//                 {
//                     turmaIndice = i;
//                     break;
//                 }  
//             }
//             if (turmaIndice == -1)
//             {
//                 printf("Turma nao encontrada\n");
//             }

//             printf("\n Turma %d\n", turmas[turmaIndice].numeroTurma);

//             for (int i = 0; i < turmas[turmaIndice].totalAlunos; i++)
//             {
//                 printf("Aluno: %s\n", turmas[turmaIndice].alunos[i].nome);

//                 printf("Matricula: %d\n", turmas[turmaIndice].alunos[i].matricula);

//                 printf("Notas: %.2f %.2f\n", 
//                 turmas[turmaIndice].alunos[i].notas[0], turmas[turmaIndice].alunos[i].notas[1]);
//                 break;
//             }

//             //     for (int j = 0; j < 2; j++)
//             //     {
//             //         printf("%.2f", turmas[turmaIndice].alunos[i].notas[j]);
//             //     }
//             //     printf("\n");
//             // }
//             // break;
        
//         default:
//         printf("Programa encerrado!\n\n");

//             break;
//         }


//     } while (opcao !=5);

//     return 0;

// }