#Gavin Woodhouse, Tatiana Susov, Andrea Lugo, Ali Walton, Quiz
import time
current = time.time()
local_time = time.localtime(current)
hour = local_time.tm_hour
#Function for score table, makes sure that after each question that is correct a point is added, score will be printed at end of game.
#Function for questions, Gavin
score = 0
def question(prompt):
    return input(f"{prompt}?\n").strip()

def answer(correct1, correct2, correct3):
    if guess == correct1 or guess == correct2 or guess == correct3:
        print("Correct!\n")
         
    else:
        print("Incorrect!\n")

#Loop to print questions with a random function, Ali
import random

num = 1
rand = random.randint(1,19)
while num < 20:
    if rand == 1:
        guess = question("Can you tell me the time")
        answer("yes", "the time", "time for you to get a watch")
        score +=1
    
    elif rand == 2:
        guess = question("What was his name-o")
        answer("bingo", "bingo", "bingo")
        score +=1
    
    elif rand == 3:
        guess = question("If you had a speech impediment/disorder, how would you pronounce it")
        answer("lithp", "stutututtering", "lysdexia")
        score +=1

    elif rand == 4:
        guess = question("I feel like giving you a freebie, just type whatever, I guess")
        answer("whatever", "whatever", "whatever")
        score +=1        
        
    elif rand == 5:
        guess = question("What is 2 + 2")
        answer("22", "4", "fish")
        score +=1

    elif rand == 6:
        guess = question("What little thing did Mary Have")        
        answer("lamb", "lamb", "lamb")
        score +=1   
    
    elif rand == 7:
        guess = question("If you are eating dumplings, what country would you likely be in")
        answer("china", "china", "china")
        score +=1

    elif rand == 8:
        guess = question("What continent would you find Togo in")
        answer("africa", "africa", "africa")
        score +=1

    elif rand == 9:
        guess = question("1,2,3,5,8,13,21,34___; what's the last number")
        answer("55", "55", "55")
        score +=1        

    elif rand == 10:
        guess = question("If the answer to a question was '24 hours', what would the question be")
        answer("how long is a day", "what is the length of a day", "how many hours are in a day")
        score +=1

    elif rand == 11:
        guess = question("What is your current score")
        answer(score, score, score)
        score +=1
        
    elif rand == 12:
        guess = question("What is the second letter of the alphabet plus the fifteenth letter of the alphabet times two")
        answer("boo", "boo", "boo")
        score +=1
        
    elif rand == 13:
        guess = question("What instrument do people usually argue over whether it is a string instrument or not")
        answer("piano", "piano", "piano")
        score +=1

    elif rand == 14:
        guess = question("How do you spell tacocat backwards")
        answer("tacocat", "tacocat", "tacocat")
        score =+1
        
    elif rand == 15:
        guess = question("Are you a robot")
        answer("no", "maybe", "wouldn't you like to know")
        score +=1

    elif rand == 16:
        guess = question("What's your name? (don't actually tell me) How do you spell it")
        answer("it", "it", "it")
        score +=1
    else:
        guess = question("If you have lived for 1095 days, how old would you be")
        answer("3", "3", "3")
        score =+1
#Conditional to say whether answer to question was correct or not, Tatianas = question("What is your current score")
#Conditional to say whether answer to question was correct or not, Tatiana