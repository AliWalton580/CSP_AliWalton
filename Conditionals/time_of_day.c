//Ali Walton, Time of Day in C
#include <stdio.h>
#include <time.h>

int main(void){
    time_t rawtime;
    struct tm * timeinfo;
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    time_t now = time(NULL);
    struct tm *tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;


    if  (hour >= 12 && hour < 17){
    printf("Good afternoon!\n");
    }else if (hour >=17){
    printf("Good evening!\n");
    }else{
    printf("Good morning!\n");
    }
    return 0;
}