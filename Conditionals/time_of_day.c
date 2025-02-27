//Ali Walton, Time of Day in C
#include <stdio.h>
#include <time.h>

time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);
    printf("Current time and date is %s\n", asctime(timeinfo));
    time_t now = time(NULL);
    struct tm *tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
    printf("%d\n", hour);
    return 0;