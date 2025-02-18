# Ali Walton, Functions Notes in Python

# Function is an action stored in a key word
#number = int(input("Can I get a number:\n"))
#def add(numOne, numTwo):#perameters go in the parenthesis seperated by commas

#def add():
    #numOne = int(input("Give me a number:\n"))
    #numTwo = int(input("Give me a number:\n"))
    #print(numOne+numTwo)

#add()

 #add(numOne, numTwo):#perameters go in the parenthesis seperated by commas
   # print(numOne+numTwo)

#add(int(input("Tell me a number\n"12, 20)), number)#arguments are givin when the function is called and must match the number of the perameters
#add(2, 4)
#add(7, 21)

def user(word):
    return  input(f"Tell me a {word}:\n")

name = user("name")
verb = user("verb")
place = user("place")
print(f"{name} was {verb} and somehow got to {place}.")