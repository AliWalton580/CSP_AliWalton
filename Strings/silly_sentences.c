//Ali Walton, Silly Sentences C
#include <stdio.h>
//string variables for my user inputs (minimum of 3)

char name[20];
char animal[20];
char verb[20];
char place[20];
char food[20];
int time;

int main(void){
     //introduce user to program... tell them what is happening (print statement)

     //create user input (print statements with questions AND scanf to collect the info)(same as the number of variables)

     //insert variables into the sentence to show the user (print statement) example: "hello %s", name
     printf("Welcome to my program, this will make a silly sentence by filling in the following blanks.\n");
     printf("Give me a name:\n");
     scanf("%s", name);
     printf("Give me a verb:\n");
     scanf("%s", verb);
     printf("Give me an animal:\n");
     scanf("%s", animal);
     printf("Give me a place:\n");
     scanf("%s", place);
     printf("Give me a food:\n");
     scanf("%s", food);
     printf("Give me a time:\n");
     scanf("%d", time);
     printf("%s is %s from a scary %s at a %s while eating their favorite food %s at %d.", name, verb, animal, place, food, time);
     return 0;
}