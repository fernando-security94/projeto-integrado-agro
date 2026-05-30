#include <stdio.h>

int main(){
    int number_1, number_2;

    printf("Type the first number: ");
    scanf("\n%d", &number_1);

    printf("Type the second number: ");
    scanf("\n%d", &number_2);
    
    printf("\n Are these two numbers equal? %d", number_1 == number_2);

    printf("\n Is the first number greater than the second? %d", number_1 > number_2);

    printf("\n Is the first number less than the second? %d", number_1 < number_2);

    return 0;
}