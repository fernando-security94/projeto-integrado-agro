#include <stdio.h>
#include <math.h>

int main(){
    char option;
    float price, total;

    printf("\nThe bill price is: $");
    scanf("\n%f", &price);

    printf("\nSelect the discount: \n");

    printf("\nA = 10%% off\n");
    printf("\nB = 20%% off\n");

    printf("\nSelect your discount: \n");
    scanf("\n%s", &option);

    switch (option)
    {
    case 'A':
        total = price - (price * 0.10);
        printf("\nThe total price is $%.2f\n", total);
        break;

    case 'B':
        total = price - (price * 0.20);
        printf("\nThe total price is $%.2f\n", total);
        break;
    
    default:
        printf("\nERROR!");
        break;
    }



    return 0;
}