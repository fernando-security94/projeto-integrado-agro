// calcular conta total
// calcular desconto em cima da conta total
// calcular a divisão da conta pelo numero de pessoas da mesa

#include <stdio.h>
#include <math.h>

int main(){
    float total_bill;
    float discount_perce;
    float bill_discount;
    float split_bill;
    int people;

    printf("Total bill: $");
    scanf("\n%f", &total_bill);

    printf("How many people: ");
    scanf("\n%d", &people);

    printf("Discount: ");
    scanf("\n%f", &discount_perce);

    bill_discount = total_bill * discount_perce/100;
    printf("\nThe discount is: $ %.2f", bill_discount);

    split_bill = (total_bill - bill_discount) / people;



   printf("\nThe bill total with discount is %.2f: ", total_bill - bill_discount);
   printf("\nThe splitted bill is %.2f: ", split_bill);




    return 0;
}