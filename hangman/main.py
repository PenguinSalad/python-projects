#!/usr/bin/env python3
import time
import random


#Init a few variables
guessedWord = []
wrongList = []
winner = False

print ("""
######################################################################
#                                                                    #
<<<<<<< HEAD
#                         wenas, ahorcado                            #
=======
#                          HANGMAN   GAME                            #
>>>>>>> 53fb8930badef3f02f7f38681fa401ed386afc1d
#                                                                    #
######################################################################
""")
while True: #Setting difficulty loop
    lives = input("Set difficulty level (Easy/Medium/Hard): ")
    if ((lives == 'e') or (lives == 'E') or (lives == 'easy') or (lives == 'Easy')):
        lives = 10
        break
    elif ((lives == 'm') or (lives == 'M') or (lives == 'medium') or (lives == 'Medium')):
        lives = 7
        break
    elif ((lives == 'h') or (lives == 'H') or (lives == 'hard') or (lives == 'Hard')):
        lives = 5
        break
print("\nYou have %d lives" % lives)
time.sleep(1)

#Choose a random word from wordlist.txt
with open("wordlist.txt") as wordlist:
    wordlist = wordlist.readlines()
keyWord = random.choice(wordlist).rstrip()
listedWord = list(keyWord)

print("\n")

#Create a blank list with '_' for each letter to guess, spaced (,end=' ')
for x in range(len(listedWord)):
    guessedWord.append("_")
    print (guessedWord[x], end=" ")

print("\n")

while (lives > 0):
    guessedLetter = input(": ").lower() #Try guessing a letter
    if (guessedLetter in wrongList): #If you already tried that letter
        print("You already tried '%s'" % guessedLetter.upper())
    else:
        for x in range(len(listedWord)):
            if ((listedWord[x]) == guessedLetter):
                guessedWord[x] = guessedLetter
            elif ((listedWord[x]) == "_"):
                guessedWord[x] = "_"
            else:
                wrongList.append(guessedLetter)
        if (guessedLetter not in listedWord):
            lives -= 1
            if (lives == 1):
                print("Wrong! You have %d live left" % lives)
            else:
                print("Wrong! You have %d lives left" % lives)
    print(' '.join(guessedWord))
    print("\n")
    if ("_" not in guessedWord):
        winner = True
        break

if winner:
    print("Congratz")
else:
    print("You lose! The word was '%s'" % keyWord.rstrip())
