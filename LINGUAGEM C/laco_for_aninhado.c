#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){
    int num, multi, x, y;


    for (num = 1; num <= 5; num++)
    {
        for (multi = 1; multi <=10; multi++)
        {
            printf("\n%d", num * multi);
        }
        printf("\n");
    }

    for(int x = 10, y = 0; x >= 0, y <= 10; x--, y++)
    {
        printf("x = %d, y = %d\n", x,y);
    }


    return 0;
}