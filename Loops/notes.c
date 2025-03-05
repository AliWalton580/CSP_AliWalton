//Ali Walton, Loops Notes in C
#include <stdio.h>

int main(void){
    // 1.What is a loop? 
        // A section of code that repeats
    // 2.What are the two types of loops?
        // for loops
        int x;
        for(x=0; x<10;x++){
            printf("Hello\n");
        }
        //While loops
        int i=1;
        while(i<10){
            printf("%d\n", i);
            i++;
        }
    // 3.What is iteration
        // The act of repeating something.
        // reference an itteration as a specific time through the loop.
    // 4.What are lists (arrays)? 
        // A bunch of values in one variable.
    // 8.How do you make lists (arrays) in C?
    int grades[] = {97, 95, 100, 70, 94, 98, 64};
        // In the brackets we say how long the list will be, if list is set there brackets can be blank
        // data type is given as whatever is in the list (All list items must be the same data type)
        // list is surroundedd by curly brackets with ommas between each item
    printf("%d\n", grades[3]); // To print one item we put the index in the rackets when we print
    grades[2] = 73;
    printf("%d\n", grades[2]); // update grades one at a time using the index number
    // This tells the the number of bytes in my array
    //printf("%lu", sizeof(grades));
    // How to get the size of an array(list)
    int length = sizeof(grades)/sizeof(grades[0]);
    printf("%d\n", length);
    // 9.How do you make for loops in C?
        // iterators should be x or i
    int t;
        //in parenthesis 1. starting point 2. go until point 3. what we count by for(t=0;t<=10;t+=2)
    for(t=0;t<5;t++){
        printf("%d\n", t);
    }
    int l;
    for(l=0; l<length; l++){
        printf("%d\n", grades[1]);
    }
    // 10.How do you make while loops in C?
    // use iterator to set start poiny
    int iterator= 100;
    // While line sets the stop point/ how long it goes
    while(iterator >=0){
        printf("%d\n", iterator);
        // Sets what I count by
        iterator -= 10;
    }

    char movies[][20] = {"Cinderella", "The Smurfs Movie", "Transformers", "Cars", "Up", "1984"};
    int mlength = sizeof(movies)/sizeof(movies[0]);
    int m = 0;
    while(m<mlength){
        printf("%s\n", movies[m]);
        m++;
    }
     return 0;
}