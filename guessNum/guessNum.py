import time
import random

#Create a cool banner
print ("-"*50)
print("\n           Welcome to Guess the Number!\n")
print("-"*50)

time.sleep(2)

randomNumbers = 20
print("I will think of a number between 1 and %d, and you'll try to guess it. Are you ready?" % randomNumbers)
time.sleep(2)

#Thinks of a random number between 1 and randomNumbers

randseq = [x + 1 for x in range (randomNumbers)]
winner = (random.choice(randseq))

while True:
    guess = eval(input("Your guess: "))
    if (guess > winner):
        print("Too high! Try again")
    elif (guess < winner):
        print("You guessed too low! Try again")
    else:
        print("You got it! It was %d" % winner)
        break
