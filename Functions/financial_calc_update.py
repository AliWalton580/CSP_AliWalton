# Ali Walton, Finacial Calculator Update Python

def info(income, amount, type):
    pertype = (amount/income)*100
    print(f"you spend ${round(amount,2)} on {type} and that is {pertype:.0f}% of your income")

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
spending = income-(rent+utilities+groceries+transportation+savings)

info(income, rent, "rent")
info(income, utilities, "utilities")
info(income, groceries, "groceries")
info(income, transportation, "transportation")
info(income, spending, "spending")
info(income, savings, "savings")