//Ali Walton, Financial Calculaotr C
#include <stdio.h>
// write a print statement telling the user what the program is (Budget calculator)

// Ask for monthly income (User input)
float income;
// Ask for rent amount (User input)
float rent;
// Ask for utilities amount (User input)
float utilities;
// Ask for groceries amount (User input)
float groceries;
// Ask for transportation amount (User input)
float transportation;
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
    printf("%s\n", "What is your monthly income:\n");
    scanf("%s\n", income);
    printf("%s\n", "What is your monthly rent cost:\n");
    scanf("%s\n", rent);
     return 0;
}