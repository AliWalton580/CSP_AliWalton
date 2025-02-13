# Ali Walton, Silly Sentences Python

print("Welcome to my program, this will make a silly sentence by filling in the following blanks.")

name = input("Give me a name:\n").strip().capitalize()

animal = input("Give me a animal:\n")

verb = input("Give me an present tense verb:\n")

time = input("Give me a time:\n")

place = input("Give me a place:\n")

food = input("Give me a food:\n")

print(f"{name} is {verb} from a scary {animal} at a {place} while eating their favorite food {food} at {time}.")