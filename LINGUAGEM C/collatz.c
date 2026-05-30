// conjectura de Collatz

#include <stdio.h>
#include <math.h>

int main(){
    int num, i;

    printf("\nDigite um numero: ");
    scanf("%d", &num);

    i = 0;

    while (num > 1)
    {
        if (num % 2 == 0)
        {
            num /= 2;
        }
        else 
        num * 3;
        num + 1;

        printf("\n%d\n", num);

        i++;
    }

    return 0;
}