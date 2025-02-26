# Ali Walton, Old Enough In Python

print("Welcome to my program, this will tell you if your are old enough to vote, drive, get a learners permit, and go to school.")

age = int(input("Please tell me your age:\n"))

if age >= 5:
    if age >= 15:
        print(f"You are old enough to get a leaners permit!")
    elif age<= 14 :
        print(f"{age} is not old enough to get a leaners permit.")
    if age >= 18:
        print(f"You are old enought to vote!")
    elif age <= 17:
        print(f"{age} is not old enough to vote.")