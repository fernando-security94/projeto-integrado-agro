#include <stdio.h>
#include <stdlib.h>

int main() {


    for (int i = 1; i <= 100; i++)
    {
        if (i % 10 == 0)
            continue;
        printf("\n%d", i);
        
    }
    
}