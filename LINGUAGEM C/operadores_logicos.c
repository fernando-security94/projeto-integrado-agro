#include <stdio.h>

int main(){

int a=5, b=10, c=5;

// A igual a B AND A igual a C
printf("\n (a==b)&&(a==c) = %d", ((a==b)&&(a==c)));

// A igual a B OR A igual a C
printf("\n (a==b)||(a==c) = %d", ((a==b)||(a==c)));

// NOT A igual a B OR A igual a C
printf("\n !(a==b)||(a==c) = %d", !((a==b)||(a==c)));

return 0;

}

