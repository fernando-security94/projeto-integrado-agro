#include <stdio.h>
#include <math.h>

int main(){
    int tv_2020 = 800;
    int laptop_2020 = 650;
    int smartphone_2020 = 1500;

    int tv_2021 = 950;
    int laptop_2021 = 550;
    int smartphone_2021 = 1800;

    int tv_2022 = 725;
    int laptop_2022 = 700;
    int smartphone_2022 = 2100;

    float average_2020 = (tv_2020 + laptop_2020 + smartphone_2020)/3;
    float average_2021 = (tv_2021 + laptop_2021 + smartphone_2021)/3;
    float average_2022 = (tv_2022 + laptop_2022 + smartphone_2022)/3;

    float average_three_years = (average_2020 + average_2021 + average_2022);

    printf("\nThe average of 2020 was %.2f\n", average_2020);
    printf("\nThe average of 2021 was %.2f\n", average_2021);
    printf("\nThe average of 2022 was %.2f\n", average_2022);

    if (average_2020 > average_2021 && average_2020 > average_2022)
    {
        printf("The year of 2020 had the greatest average");
    }

    else if (average_2021 > average_2020 && average_2021 > average_2022)
    {
        printf("The year of 2021 had the greatest average\n");
    }

    else
    {
        printf("\nThe year of 2022 had the greatest average");
    }
    
    
    

    // printf("\nDid the year of 2020 have the greater average %d\n",
    // (average_2020 > average_2021) && (average_2020 > average_2022));

    // printf("\nDid the year of 2021 have the greater average? %d\n",
    //     (average_2021 > average_2020) || (average_2021 > average_2022));
        
    // printf("\nDid the year of 2022 have the greater average? %d\n",
    //     (average_2022 > average_2020) || (average_2022 > average_2021));
            
        
    

    return 0;
}