// Calcular massa de C
// sendo C = A + B
// A = 321,43
// B = 150.72

#include <stdio.h>

const float comp_a = 321.43;
const float comp_b = 150.72;

int main(){
    // A = 1.2 B = 1.0
    printf("\nMol A: 1.2, Mol B: 1.0");
    printf("\nMol C: %.2f\n", (1.2 *comp_a) + (1 * comp_b));

    // A = 1.4 B =1.0
    printf("\nMol A: 1.4, Mol B: 1.0");
    printf("\nMol C: %.2f\n", (1.4 *comp_a) + (1 * comp_b));

    // A = 1.0 B = 1.6
    printf("\nMol A: 1.0, Mol B: 1.6");
    printf("\nMol C: %.2f\n", (1.0 *comp_a) + (1.6 * comp_b));
    


}