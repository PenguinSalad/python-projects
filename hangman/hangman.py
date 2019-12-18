#!/usr/bin/env python3
import time
import random

#Maybe add difficulty levels? (More tries per word)
#You have X lifes, try guess the most words. When you lose all lives you lose

#Print a _ _ _ _ for each letter and you type a letter
#If you guess it right it appears _ _ _ A

#If not, _ _ _ _ you lose a life

#When you have the full word - (Maybe make it so another word appears?) or end game

######################################################################
#                                                                    #
#                         WELCOME MESSAGE                            #
#                                                                    #
######################################################################

# while True: #Setting difficulty loop
#     lives = input("Set difficulty level (Easy/Medium/Hard): ")
#     if ((lives == 'e') or (lives == 'E') or (lives == 'easy') or (lives == 'Easy')):
#         lives = 7
#         break
#     elif ((lives == 'm') or (lives == 'M') or (lives == 'medium') or (lives == 'Medium')):
#         lives = 5
#         break
#     elif ((lives == 'h') or (lives == 'H') or (lives == 'hard') or (lives == 'Hard')):
#         lives = 3
#         break


#Choose a random word from wordlist.txt
with open("wordlist.txt") as wordlist:
    wordlist = wordlist.readlines()
keyWord = random.choice(wordlist)
listedWord = list(keyWord)
while True:
    print("_ "*len(keyWord))
    print("\n")
    #print(keyWord)
    guessedLetter = input(": ")
    for x in range(len(keyWord)):
        if ((listedWord[x]) == guessedLetter):
            print(guessedLetter, end = " ")
        else:
            print("_", end = " ")
