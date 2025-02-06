//Ali Walton, First Program in C
#include <stdio.h>

char name[20];

int main(void){
    printf("Hello, what is your name:\n");
    fgets(name, sizeof(name), stdin);

    printf("Hello %s", name);
    return 0;
}