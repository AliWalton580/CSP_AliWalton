//Ali Walton, Financial Calculaotr C
#include <stdio.h>
// write a print statement telling the user what the program is (Budget calculator)

// Ask for monthly income (User input)

// Ask for rent amount (User input)

// Ask for utilities amount (User input)

// Ask for groceries amount (User input)

// Ask for transportation amount (User input)

// Calculate savings as 10% of income (variable)

// Calculate spending money income - (rent-utilities-groceries-transportation-savings) (variable)

// Calculate percent of rent (rent/income)*100 (variable)

// Calculate percent of utilities (utilities/income)*100 (variable)

// Calculate percent of groceries (groceries/income)*100 (variable)

// Calculate percent of transportation (transportation/income)*100 (variable)

// Calculate percent of spending (spending/income)*100 (variable)

// tell user catagorie spending amount AND percent for rent ("you spend $XX.XX on rent and that is XX% of your income")

// tell user catagorie spending amount AND percent for utilities ("you spend $XX.XX on utilities and that is XX% of your income")

// tell user catagorie spending amount AND percent for groceries ("you spend $XX.XX on groceries and that is XX% of your income")

// tell user catagorie spending amount AND percent for transportation ("you spend $XX.XX on transportaion and that is XX% of your income")

// tell user catagorie spending amount AND percent for spending ("you spend $XX.XX on spending and that is XX% of your income")

// tell user catagorie spending amount AND percent for savings ("you spend $XX.XX on savings and that is 10% of your income")

int main(void){
    printf("Welcome to my program, this financial calculator will tell you your monthly spending amount on different expensses and the percentage cost of your monthly income.\n");
    float income;
    printf("What is your monthly income:\n");
    scanf("%f", &income);
    float rent;
    printf("What is your monthly rent:\n");
    scanf("%f", &rent);
    float utilities;
    printf("What is your monthly utilities cost:\n");
    scanf("%f", &utilities);
    float groceries;
    printf("What is your monthly grocerie cost:\n");
    scanf("%f", &groceries);
    float transportation;
    printf("What is your monthly transportation:\n");
    scanf("%f", &transportation);

    float savings = income*0.1;
    float spending = income-rent-utilities-groceries-transportation-savings;
    float rentpercent = (rent/income)*100;
    float utilitiespercent = (utilities/income)*100;
    float groceriespercent = (groceries/income)*100;
    float transportationpercent = (transportation/income)*100;
    float spendingpercent = (spending/income)*100;
    printf("You spend $%.2f on rent and that is %.2f%% your income.\n", rent, rentpercent);
    printf("You spend $%.2f on utilities and that is %.2f%% of your income\n", utilities, utilitiespercent);
    printf("You spend $%.2f on groceries and that is %2.f%% of your income.\n", groceries, groceriespercent);
    printf("You spend $%.2f on transportation and that is %2.f%% of your income.\n", transportation, transportationpercent);
    printf("You spend $%.2f on spending and that is %2.f%% of your income.\n", spending, spendingpercent);
    printf("You spend $%.2f on savings and that is 10%% of your income.\n", savings);
     return 0;
}