//Ali Walton, Name decorator C
#include <stdio.h>
#include <string.h>

char name[20];

int main(void){
     char dec[] = "~~~ ";
     char dec2[] = " ~~~";
     printf("What is your name?\n");
     scanf("%s", name);
     strcat(dec, name);
     printf("%s", dec);
     strcat(name, dec2);
     printf("%s", dec2);
     return 0;
}