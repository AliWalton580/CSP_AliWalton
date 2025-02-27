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


    if  (hour <= 17){
    printf("Good Evening!");
    }else if (hour >=12){
    printf("Good afternoon!");
    }else if (hour < 12){
    printf("Good morning!");
    }
    return 0;
}