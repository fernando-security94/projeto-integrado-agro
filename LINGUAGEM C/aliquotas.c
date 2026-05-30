#include <stdio.h>
#include <math.h>

int main(){
    float salario_bruto;
    float aliquota_inss;
    float aliquota_ir;
    float salario_liquido;

    printf("\nDigite seu salario: $");
    scanf("\n%f", &salario_bruto);
    
    // Aliquota INSS

    if (salario_bruto <= 1320)
    {
        aliquota_inss = salario_bruto * 0.0075;
        printf("\nAliquota de INSS: $%.2f\n", aliquota_inss);
    }
    else if (salario_bruto >=1320.01 && salario_bruto <=2571.29)
    {
        aliquota_inss = salario_bruto * 0.009;
        printf("\nAliquota de INSS: $%.2f\n", aliquota_inss);
    }
    else if (salario_bruto >=2571.30 && salario_bruto <=3856.94)
    {
        aliquota_inss = salario_bruto * 0.12;
        printf("\nAliquota de INSS: $%.2f\n", aliquota_inss);
    }
    else if (salario_bruto >=3856.95 && salario_bruto <=7505.49)
    {
        aliquota_inss = salario_bruto * 0.14;
        printf("\nAliquota de INSS: $%.2f\n", aliquota_inss);
    }
    else
    aliquota_inss = 1051.04;
    printf("Aliquota maxima INSS: $%.2f", aliquota_inss);

    
    // Aliquota IR
    if (salario_bruto <= 1903.98)
    {
        printf("\nSem desconto de IR");
    }
    else if (salario_bruto >=1903.99 && salario_bruto <= 2826.65)
    {
        aliquota_ir = salario_bruto * 0.0075;
        printf("\nAliquota IR: $%.2f\n", aliquota_ir);
    }
    else if (salario_bruto >=2826.66 && salario_bruto <= 3751.05)
    {
        aliquota_ir = salario_bruto * 0.15;
        printf("\nAliquota IR: $%.2f\n", aliquota_ir);
    }
    else if (salario_bruto >=3751.06 && salario_bruto <= 4668.68)
    {
        aliquota_ir = salario_bruto * 0.225;
        printf("\nAliquota IR: $%.2f\n", aliquota_ir);
    }
    else if (salario_bruto >4668.68 )
    {
        aliquota_ir = salario_bruto * 0.275;
        printf("\nAliquota IR: $%.2f\n", aliquota_ir);

        salario_liquido = salario_bruto - aliquota_inss - aliquota_ir;
        printf("\nSALARIO LIQUIDO: $%2.f", salario_liquido);
    }
    

    
    return 0;
}