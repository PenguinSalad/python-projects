from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Ultimate Bravery")
""" root.iconbitmap("images/gnarIcon.ico") """


aatrox = {
    "diff": 7,
    "mainRune": "fleet"
}

akali = {
    "diff": 8,
    "mainRune": "conq"
}

champList = [aatrox, akali]


def matchupFinder():
    matchup = matchupEntry.get()
    matchupEntry.delete(0, END)
    matchupLabel = Label(root, text=matchup)
    matchupLabel.grid(row=1, column=0)



matchupEntry = Entry(root)
matchupEntry.grid(row=0, column=0)

submitEntry = Button(root, text="Go", command = matchupFinder)
submitEntry.grid(row=0, column=1)

exitBtn = Button(root, text="Exit", command = root.quit)
exitBtn.grid(row=2, column=0)









""" img = ImageTk.PhotoImage(Image.open("images/Bard_0.jpg"))
label = Label(image=img)
label.pack() """




root.mainloop()
