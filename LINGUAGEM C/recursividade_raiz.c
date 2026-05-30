// Crie a função calcularRaiz(), que recebe dois parâmetros: 
// o valor a ser calculado e a raiz anterior, 
// inicialmente definida como o chute inicial.
// Implemente a fórmula sugerida pelos matemáticos usando a função pow().
// Calcule a diferença entre o valor obtido no passo 2 
// e o valor da raiz anterior e verifique se é menor que o critério de parada:
// Se for o caso, o valor é satisfatório e pode ser retornado. 
// Caso contrário, a função calcularRaiz() deve ser chamada novamente, 
// passando como parâmetro o número e a raiz obtida no passo 2. 

#include <stdio.h>
#include <math.h>

float calcularRaiz(float numero, float raizAnt){
    float raiz = (pow(raizAnt, 2) + numero) / (2 * raizAnt);

    if (fabs(raiz - raizAnt) < 0.001)
        return raiz;
    return calcularRaiz(numero, raiz);
}

void main(){
    float numero, result;

    printf("Digite numero para calcular raiz quadrada: ");
    scanf("%f", &numero);

    result = calcularRaiz(numero, numero/2);
    printf("\nRaiz quadrada de %.2f = %.2f", numero, result);

}