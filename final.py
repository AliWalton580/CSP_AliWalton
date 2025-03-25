#Gavin Woodhouse, Tatiana Susov, Andrea Lugo, Ali Walton, Quiz

#Function for score table, makes sure that after each question that is correct a point is added, score will be printed at end of game.
#Function for questions, Gavin

score = 0

def question(prompt):
    return input(f"{prompt}?\n").strip().lower()

def answer(correct1, correct2, correct3):
    global score
    if guess == correct1 or guess == correct2 or guess == correct3:
        print("Correct!\n")
        score +=1      
    else:
        print("Incorrect!\n")

#Loop to print questions with a random function, Ali
import random

num = 1
while num <= 10:
    rand = random.randint(1,19)
    if rand == 1:
        guess = question("Can you tell me the time")
        answer("yes", "the time", "time for you to get a watch")
        num +=1
    
    elif rand == 2:
        guess = question("What was his name-o")
        answer("bingo", "bingo", "bingo")
        num +=1
        rand != 2
    
    elif rand == 3:
        guess = question("If you had a speech impediment/disorder, how would you pronounce it")
        answer("lithp", "stutututtering", "lysdexia")
        num +=1
        rand != 3

    elif rand == 4:
        guess = question("I feel like giving you a freebie, just type whatever, I guess")
        answer("whatever", "whatever", "whatever")
        num +=1
        rand != 4        
        
    elif rand == 5:
        guess = question("What is 2 + 2")
        answer("22", "4", "fish")
        num +=1
        rand != 5

    elif rand == 6:
        guess = question("What little thing did Mary Have")        
        answer("lamb", "lamb", "lamb")
        num +=1
        rand != 6   
    
    elif rand == 7:
        guess = question("If you are eating dumplings, what country would you likely be in")
        answer("china", "china", "china")
        num +=1
        rand != 7

    elif rand == 8:
        guess = question("What continent would you find Togo in")
        answer("africa", "africa", "africa")
        num +=1
        rand != 8

    elif rand == 9:
        guess = question("1,2,3,5,8,13,21,34___; what's the last number")
        answer("55", "55", "55")
        num +=1
        rand != 9        

    elif rand == 10:
        guess = question("If the answer to a question was '24 hours', what would the question be")
        answer("how long is a day", "what is the length of a day", "how many hours are in a day")
        num +=1
        rand != 10

    elif rand == 11:
        guess = question("nuf gnivaH")
        answer("sey", "on", "ebyam")
        num +=1
        rand != 11
        
    elif rand == 12:
        guess = question("What is the second letter of the alphabet plus the fifteenth letter of the alphabet times two")
        answer("boo", "boo", "boo")
        num +=1
        rand != 12
        
    elif rand == 13:
        guess = question("What instrument do people usually argue over whether it is a string instrument or not")
        answer("piano", "piano", "piano")
        num +=1
        rand != 13

    elif rand == 14:
        guess = question("How do you spell tacocat backwards")
        answer("tacocat", "tacocat", "tacocat")
        num +=1
        rand != 14
        
    elif rand == 15:
        guess = question("Are you a robot")
        answer("no", "maybe", "wouldn't you like to know")
        num +=1
        rand != 15

    elif rand == 16:
        guess = question("What's your name? (don't actually tell me) How do you spell it")
        answer("it", "it", "it")
        num +=1
        rand != 16

    elif rand == 17:
        guess = question("If you have lived for 1095 days, how old would you be")
        answer("3", "3 years old", "1095 days")
        num +=1
        rand != 17

    elif rand == 18:
        guess = question("Before you read the rest of this question, read the emancipation proclamation. What color was the author's eyes")
        answer("hazel", "gray", "hazel gray")
        num +=1
        rand != 18

    elif rand == 19:
        guess = question("Before you read the rest of this question, read the emancipation proclamation. What color was the author's eyes")
        answer("hazel", "gray", "hazel gray")
        num +=1
        rand != 19

#Conditional to say whether answer to question was correct or not, Tatiana
if score == 10:
    print(f"You got all corect, your really smart!")
elif score == 9:
    print(f"You only missed one question!")
elif score == 8:
    print(f"You got 8 out of ten correct!")
elif score == 7:
    print(f"You got 7 out of ten correct")
    