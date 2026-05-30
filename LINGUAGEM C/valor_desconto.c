//preço de venda de um televisor seja de R$ 1500.00. 
// Vamos considerar que a taxa de imposto aplicável seja de 10%,
// e que haja um desconto padrão de 5% para esse produto em particular.


#include <stdio.h>
#include <math.h>

int main(){
    // variaveis
    float sell_price, taxes_price, discount_price,
    final_price;

    // constantes
    const float taxes = 0.1;
    const float stand_discount = 0.05;

    // entrada de dado
    printf("Sell price: $");
    scanf("\n %f", &sell_price);

    // processamento
    taxes_price = sell_price * taxes;
    discount_price = sell_price * stand_discount;

    final_price = sell_price + taxes_price - discount_price;

    printf("The total price of taxes is $%.2f\n", taxes_price);

    printf("The total discount is $%.2f\n", discount_price);

    printf("The final price is $%.2f", final_price);

    return 0;

}