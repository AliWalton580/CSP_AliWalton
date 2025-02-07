# Ali Walton, Finacial Calculator Python

# write a print statement telling the user what the program is (Budget calculator)
print("Welcome to my program, this financial calculator will tell you your monthly spending amount on different expensses and the percentage cost of your monthly income.")
# Ask for monthly income (User input)
income = float(input("What is your monthly income\n"))
# Ask for rent amount (User input)
rent = float(input("What is your monthly rent\n"))
# Ask for utilities amount (User input)
utilities = float(input("What is your monthly utilities cost\n"))
# Ask for groceries amount (User input)
groceries = float(input("What is your monthly grocerie cost\n"))
# Ask for transportation amount (User input)
transportation = float(input("What is your monthly transportation cost\n"))
# Calculate savings as 10% of income (variable)
savings = income*0.1
# Calculate spending money income - (rent-utilities-groceries-transportation-savings) (variable)
spending = income-rent-utilities-groceries-transportation-savings
# Calculate percent of rent (rent/income)*100 (variable)
rentpercent = (rent/income)*100
# Calculate percent of utilities (utilities/income)*100 (variable)
utilitiespercent = (utilities/income)*100
# Calculate percent of groceries (groceries/income)*100 (variable)
groceriespercent = (groceries/income)*100
# Calculate percent of transportation (transportation/income)*100 (variable)
transportpercent = (transportation/income)*100
# Calculate percent of spending (spending/income)*100 (variable)
spendingpercent = (spending/income)*100
# tell user catagorie spending amount AND percent for rent ("you spend $XX.XX on rent and that is XX% of your income")
print(f"you spend ${rent} on rent and that is {rentpercent:.2f}% of your income")
# tell user catagorie spending amount AND percent for utilities ("you spend $XX.XX on utilities and that is XX% of your income")
print(f"you spend ${utilities} on utilities and that is {utilitiespercent:.2f}% of your income")
# tell user catagorie spending amount AND percent for groceries ("you spend $XX.XX on groceries and that is XX% of your income")
print(f"you spend ${groceries} on groceries and that is {groceriespercent:.2f}% of your income")
# tell user catagorie spending amount AND percent for transportation ("you spend $XX.XX on transportaion and that is XX% of your income")
print(f"you spend ${transportation} on transportation and that is {transportpercent:.2f}% of your income")
# tell user catagorie spending amount AND percent for spending ("you spend $XX.XX on spending and that is XX% of your income")
print(f"you spend ${spending} on spending and that is {spendingpercent:.2f}% of your income")
# tell user catagorie spending amount AND percent for savings ("you spend $XX.XX on savings and that is 10% of your income")
print(f"you spend ${savings} on savings and that is 10% of your income")