//Ali Walton, Functions Notes in C
#include <stdio.h>
// don't return strings (only for C)

void add(int numOne,int numTwo){
    printf("%d\n", numOne+numTwo);
}


int main(void){
    printf("Hello World\n");
    add(4,9);
    add(1000,2);
    add(47,9);
    add(82,3);
     return 0;
}