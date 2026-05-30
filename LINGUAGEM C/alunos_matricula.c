// Você trabalha em uma instituição educacional 
// e recebeu uma tarefa relacionada à administração de disciplinas 
// e controle de alunos matriculados. Você precisa criar um sistema 
// que gerencia o número de alunos matriculados em cada disciplina da instituição.
// Nesse cenário, o programa deve permitir
// que o administrador insira o número de disciplinas disponíveis e, 
// em seguida, para cada disciplina, o número de alunos matriculados. 
// O programa deve estar preparado para controlar a entrada de dados e interromper
// a contagem de disciplinas se 
// o número total de alunos matriculados atingir um certo limite.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

    int total_disciplinas, limite_alunos = 100,
    total_alunos = 0;

    printf("\nInsira o numero de discplinas disponiveis: ");
    scanf("%d", &total_disciplinas);

    for (int i = 1; i <= total_disciplinas; i++)
    {
        int alunos_matriculados;

        printf("\nInsira o numero de alunos matriculados na disciplina: ");
        scanf("%d", &alunos_matriculados);

        // verifica se o numero de alunos e valido
        if (alunos_matriculados < 0)
        {
            printf("\nNumero de alunos invalido. Tente novamente");
            continue;
        }
        total_alunos += alunos_matriculados;
        
        // verifica se limite de alunos foi atingido
        if (total_alunos >= limite_alunos)
        {
            printf("\nLimite de alunos atingido. Encerrando contagem.");
            break;
        }
        

    }
    printf("\nTodas as disciplinas contadas: %d\n", total_disciplinas);
    printf("\nTotal de alunos matriculados: %d\n", total_alunos);
    
    
    return 0;
}