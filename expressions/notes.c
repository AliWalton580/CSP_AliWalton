// Ali Walton, Expressions Notes C
#include <stdio.h>
// integers int when we set the variable and %d when we print
// floats float when we set the variable and %f when we print
// strings (words) char when we set the variable and %s when we print
int mynum;
float percent;

int main(void){
 printf("type a number: \n");
 scanf("%d", &mynum);
 printf("You inputed %d", mynum);
 scanf("%f", &percent);
 printf("Your persent is %f\n", percent);
 return 0;
}