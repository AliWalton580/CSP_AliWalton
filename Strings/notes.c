//Ali Walton, Strings Notes C
#include <stdio.h>
#include <string.h>

char name[20];

int main(void){
   //printf("Please tell me your full name");
   //scanf("%s", name);
   //fgets(name, 20, stdin);
   //printf("Hello %s, welcome to my program");
   // char sentence[] = "The quick fox jumps over the lazy log"
   //printf("lu\n", sizeof(sentence));
   //print("%d\n", strlen(sentence));
   char one[] = "Hello ";
   char two[] = "World!";
   char three[] = "This is my program. ";
   two[5] = '?'; //if chnages are made
   printf("%s\n", one);
   strcat(one,two);
   printf("%s\n", one);
   strcat(three, one);
   printf("%s", three);
     return 0;
}