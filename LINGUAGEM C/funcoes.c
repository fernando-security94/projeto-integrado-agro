#include <stdio.h>

// funcao somar
int somar(){
    return 2 + 3;
}

int outraSoma(int x, int y){
    int s = 0;

    s = x + y;
    return s;
}


int main(){
    int resultado = 0;
    int outroResult = 0;

    resultado = somar();
    outroResult = outraSoma(5, 4);

    printf("\nResultado primeira funcao: %d", resultado);
    printf("\nResultado segunda funcao: %d", outroResult);

    return 0;

}
