import random
from tkinter import *

root = Tk()

def diceRoll():
    randomNum = random.randint(1,6)
    myLabel = Label(root, text=randomNum)
    myLabel.pack()

myButton = Button(root, text="Dice roll", command=diceRoll)
myButton.pack()

root.mainloop()
