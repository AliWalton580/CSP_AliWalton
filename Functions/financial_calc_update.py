# Ali Walton, Finacial Calculator Update Python

print("Welcome to my program, this financial calculator will tell you your monthly spending amount on different expensses and the percentage cost of your monthly income.")

def info(income, amount, type):
    pertype = (amount/income)*100
    print(f"you spend ${round(amount,2)} on {type} and that is {pertype:.0f}% of your income")
    
    
def user(type):
    return float (input (f"What is your monthly cost of {type}?\n"))
    
income = user("income")
rent = user("rent")
utilities = user("utilities")
groceries = user("groceries")
transportation = user("transportation")
savings = income*0.1
spending = income-(rent+utilities+groceries+transportation+savings)
   
info(income, rent, "rent")
info(income, utilities, "utilities")
info(income, groceries, "groceries")
info(income, transportation, "transportation")
info(income, spending, "spending")
info(income, savings, "savings")