//Ali Walton, Update Hello World in C
#include <stdio.h>

void greet(char name[]){
    printf("Hello %s\n", name);
}

int main(void){
    greet("Olivia");
    greet("Max");
    greet("Samantha");
    greet("Pepper");
    greet("Alex");
    return 0;
}