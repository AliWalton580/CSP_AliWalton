# Ali Walton, Conditional Notes Python

#print("Hello, welcome to my program that will sort you into a catagory.")

#name = input("What is your name:\n")

#if name == "Vienna":
    #print("oh your the teacher. . . never mind.")
#else:
    #print("You are a student. Welcome to class.")



#num = int(input("how many would you like(give me a number above 0):\n"))
#conditionals start at the top and work their way down, only take the first condition that is correct
#if num == 1: #top condition should be the least likely
   # print("You have asked for an item")
#elif num <= 3:
    #print("You have asked a couple of the item")
#elif num <= 5:
    #print("You have asked for a few of the items. . . or your in the south and you aked for a couple")
#else:
    #print("You have asked for some of the item")


#name = "Katie"

#if "a" not in name:
    #print("You name has the letter A!")
#else:
    #print("You name doesn't have an A.")


#name = "Katie"

#if "a" in name or "e" in name or "i" in name or "o" in name or "u" in name:
    #print("You name has a vowel!")
#else:
    #print("You name doesn't have a vowel.")


num = 6

if num > 5 and num < 10:
    if num == 7:
        print("That is an unlucky number!")
    else:
        print(f"{num} is a large single digit number")
else:
    #if num > 10:
        #print(f"{num} is not a single digit number")
    print(f"That is {num}")