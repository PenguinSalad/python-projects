import time
import random

#Create a cool banner
print ("-"*50)
print("\nWelcome to Rock, Paper, Scissors!\n")
print("-"*50)
print("\n")
time.sleep(2)

#Init variables
options = ["Rock", "Paper", "Scissors"]
loseCount = 0
winCount = 0
askAgain = False
gameOver = False

#Main game loop
while True:
    #We randomly generate the computer's choice
    aiChoice = random.randint(0,2)

    #We input our choice
    while True: #We keep asking for input until it's a right format
        userChoice = (eval(input("Rock(1)//Paper(2)//Scissors(3):  ")))-1
        if ((userChoice == 0) or (userChoice == 1) or (userChoice == 2)):
            break
        else:
            print("Please choose a correct answer")

    print("Computer chose %s, and you chose %s" % (options[aiChoice], options[userChoice]))

    if (aiChoice == userChoice):
        print("It's a draw, go again!\n")
    elif (((aiChoice == 0) and (userChoice == 2)) or ((aiChoice == 1) and (userChoice == 0)) or ((aiChoice == 2) and (userChoice == 1))):
        print("You lose!\n")
        loseCount += 1 #Adds 1 to the number of games lost
        askAgain = True
    else:
        print("You win!\n")
        winCount += 1 #Adds 1 to the number of games won
        askAgain = True

    time.sleep(1)
    while askAgain: #Ask if you want to play again
        again = input("Do you want to play again? (Y/n)  ")
        if ((again == "y") or again == "Y" or again == "yes" or again == "Yes" or again == "YES"):
            gameOver = False
            break
        elif ((again == "n") or again == "N" or again == "no" or again == "No" or again == "NO"):
            gameOver = True
            break
        else:
            print("Please enter a correct answer")

    if gameOver: #GAME OVER screen with win/lose counters
        print("-"*50)
        print("\nThanks for playing!")
        print("You won a total of %d times, and lost %d times\n" % (winCount, loseCount))
        print("-"*50)
        break
