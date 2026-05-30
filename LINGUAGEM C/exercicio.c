#include <stdio.h>

int main(){
    int x = 42;
    int *ponteiro = &x;

    (*ponteiro) += 8;

    printf("O valor de x e: %d\n", x);

    return 0;
}