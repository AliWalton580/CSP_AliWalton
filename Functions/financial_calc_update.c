//Ali Walton, Financial Calculaotr Update in C
#include <stdio.h>

    float income;
    float rent;
    float utilities;
    float groceries;
    float transportation;
    float spending;
    float savings;

void info(float income, float amount, char type[]){
    float per = (amount/income)*100;
    printf("you spend $%.2f on %s and that is %.0f%% of your income.\n", amount, type , per);
}

float user(float amount, char type[]){
    printf("What is you monthly %s:\n", type);
    scanf("%f", &amount);
    return amount;
}

int main(void){
    printf("Welcome to my program, this financial calculator will tell you your monthly spending amount on different expensses and the percentage cost of your monthly income.\n");

    float income = user(income, "income");
    float rent = user(rent, "rent");
    float utilities = user(utilities, "utilities");
    float groceries = user(groceries, "groceries");
    float transportation = user(transportation, "transportation");
    savings = income*0.1;
    spending = income-(rent+utilities+groceries+transportation+savings);

    info(income, rent, "rent");
    info(income, utilities, "utilities");
    info(income, groceries, "groceries");
    info(income, transportation, "transportation");
    info(income, spending, "spending");
    info(income, savings, "savings");
     return 0;
}