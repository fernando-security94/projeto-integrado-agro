// Realizar a media de duas notas

#include <stdio.h>
#include <math.h>

int main(){
    float grade_1, grade_2, average;
    printf("Type the first grade: ");
    scanf("%f", &grade_1);
    printf("Type the second grade: ");
    scanf("%f", &grade_2);
    average = (grade_1 + grade_2) / 2;
    printf("Your average grade is %.2f", average);
    
    return 0;
}