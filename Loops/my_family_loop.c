//Ali Walton, My Family Loop in C
#include <stdio.h>

int main(void){
   char family[][20] = {"Caleb", "Sam", "Alex", "Peter"};
    int ilength = sizeof(family)/sizeof(family[0]);
    int i = 0;
    while(i<ilength){
        printf(" Hello, %s\n.", family[i]);
        i++;
    }
     return 0;
}