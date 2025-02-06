# Ali Walton, Finacial Calculator Python

# write a print statement telling the user what the program is (Budget calculator)

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
# Calculate percent of rent (rent/income) (variable)
rentpercent = (rent/income)*100
# Calculate percent of utilities (utilities/income) (variable)
utilitiespercent = (utilities/income)*100
# Calculate percent of groceries (groceries/income) (variable)
groceriespercent = (groceries/income)*100
# Calculate percent of transportation (transportation/income) (variable)
tranportpercent = (transportation/income)*100
# Calculate percent of spending (spending/income) (variable)
spendingpercent = (spending/income)*100
# tell user catagorie spending amount AND percent for rent ("you spend $XX>XX on rent and that is XX% of your income")
print("you spend")
# tell user catagorie spending amount AND percent for utilities ("you spend $XX>XX on utilities and that is XX% of your income")
print("you spend")
# tell user catagorie spending amount AND percent for groceries ("you spend $XX>XX on groceries and that is XX% of your income")
print("you spend")
# tell user catagorie spending amount AND percent for transportation ("you spend $XX>XX on transportaion and that is XX% of your income")
print("you spend")
# tell user catagorie spending amount AND percent for spending ("you spend $XX>XX on spending and that is XX% of your income")
print("you spend")
# tell user catagorie spending amount AND percent for savings ("you spend $XX>XX on savings and that is 10% of your income")
print("you spend")