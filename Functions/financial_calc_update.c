//Ali Walton, Financial Calculaotr Update in C
#include <stdio.h>

float income;
float rent;
float utilities;
float groceries;
float transportation;
float savings;
float spending;

void info(float income, float amount, char type[]){
    float per = (amount/income)*100;
    printf("you spend $%.2f on %s and that is %.0f%% of your income.\n", amount, type , per);
}

float user(char type[]){
    char type = ("What is your monthly cost of %s?", type);
    return 0;
}

// write a print statement telling the user what the program is (Budget calculator)

// Ask for monthly income (User input)

// Ask for rent amount (User input)

// Ask for utilities amount (User input)

// Ask for groceries amount (User input)

// Ask for transportation amount (User input)

// Calculate savings as 10% of income (variable)

// Calculate spending money income - (rent-utilities-groceries-transportation-savings) (variable)

int main(void){
    printf("Welcome to my program, this financial calculator will tell you your monthly spending amount on different expensses and the percentage cost of your monthly income.\n");

     income = user("income");
     rent = user("rent");
     utilities = user("utilities");
     groceries = user("groceries");
     transportation = user("transportation");
     savings = income*0.1;
     spending = income-rent-utilities-groceries-transportation-savings;

    info(income, rent, "rent");
    info(income, utilities, "utilities");
    info(income, groceries, "groceries");
    info(income, transportation, "transportation");
    info(income, spending, "spending");
    info(income, savings, "savings");
     return 0;
}