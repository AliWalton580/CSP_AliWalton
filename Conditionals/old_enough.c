//Ali Walton, Old Enough in C
#include <stdio.h>
#include <string.h>

int age;

int main(void){
    printf("Please tell me your age:\n");
    scanf("%d", &age);
   
    if (age >= 18){
        printf("You are old enough to have a leaners permit, go to school, vote and drive!");
    }else if (age >= 16){
        printf("You are old enogh to have a learners permit, drive, and go to school! You are not old enough to vote.");
    }else if (age >= 15){
        printf("You are old enough to get a learners permit and go to school! But not old enough to vote, or drive.");
    }else if (age >= 5){
        printf("You are old enough to go to school! You are not old enough to have a learners permit, drive or vote.");
    }else{
        printf("If you are %d, you cannot drive, go to school, vote or have a learners permit.", age);
    }
     return 0;
}