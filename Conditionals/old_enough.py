# Ali Walton, Old Enough In Python

print("Welcome to my program, this will tell you if your are old enough to vote, drive, get a learners permit, and go to school.")

age = int(input("Please tell me your age:\n"))

if age >= 18:
    print(f"You are old enough to have a leaners permit, go to school, vote and drive!")
elif age >= 16:
    print(f"You are old enogh to have a learners permit, drive, and go to school! You are not old enough to vote.")
elif age >= 15:
     print(f"You are old enough to get a learners permit and go to school! But not old enough to vote, or drive.")
elif age >= 5:
    print(f"You are old enough to go to school! You are not old enough to have a learners permit, drive or vote.")
else:
    print(f"If you are {age}, you cannot drive, go to school, vote or have a learners permit.")