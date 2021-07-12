import random

board = ''' 
   a     b     c
      |     |     
1  %s  |  %s  |  %s  
 _____|_____|_____
      |     |     
2  %s  |  %s  |  %s  
 _____|_____|_____
      |     |     
3  %s  |  %s  |  %s  
      |     |     

'''

logicBoard = [["", "", ""],
        ["", "", ""],
        ["", "", ""]]

turnOrder = []

running = True

def blankBoard():
    for i in range(3):
        for j in range(3):
            logicBoard[i][j] = "-"      


def currentBoard():
    return (board % (logicBoard[0][0], logicBoard[0][1], logicBoard[0][2], logicBoard[1][0], logicBoard[1][1], logicBoard[1][2], logicBoard[2][0], logicBoard[2][1], logicBoard[2][2]))

#print(currentBoard())

def playerMove():
    while True:
        square = input("Choose a cell: ").lower()


        row = square[0]
        col = square[1]

        row = int(row) - 1

        if col == 'a':
            col = 0
        elif col == 'b':
            col = 1
        elif col == 'c':
            col = 2

        squareValue = [row, col]

        if logicBoard[squareValue[0]][squareValue[1]] != '-':
            print("Can't pick a non-empty cell")
        else:
            break

    return squareValue


def computerMove():
    while True:
        squareValue = [random.randint(0, 2), random.randint(0, 2)]
        if logicBoard[squareValue[0]][squareValue[1]] == '-':
            break
    return squareValue

def whoStarts():
    while True:
        sign = input("Do you want to play as X or O? ").lower()

        if sign == 'x':
            turnOrder = ['X', 'O']
            return turnOrder
            break
        elif sign == 'o':
            turnOrder = ['O', 'X']
            return turnOrder
            break
        else:
            print("Wrong input")


def checkWin():

    if (logicBoard[0][0] == logicBoard[0][1] == logicBoard[0][2]) and (logicBoard[0][0] != '-'): 
        print("You win, %s" % logicBoard[0][0])
        return True

        #    a     b     c
        #       |     |     
        # 1  X  |  X  |  X  
        #  _____|_____|_____
        #       |     |     
        # 2  -  |  -  |  -  
        #  _____|_____|_____
        #       |     |     
        # 3  -  |  -  |  -  
        #       |     |     


    elif (logicBoard[1][0] == logicBoard[1][1] == logicBoard[1][2]) and (logicBoard[1][0] != '-'):
        print("You win, %s" % logicBoard[1][0])
        return True

        #    a     b     c
        #       |     |     
        # 1  -  |  -  |  -  
        #  _____|_____|_____
        #       |     |     
        # 2  X  |  X  |  X  
        #  _____|_____|_____
        #       |     |     
        # 3  -  |  -  |  -  
        #       |     |     


    elif (logicBoard[2][0] == logicBoard[2][1] == logicBoard[2][2]) and (logicBoard[2][0] != '-'):
        print("You win, %s" % logicBoard[2][0])
        return True

        #    a     b     c
        #       |     |     
        # 1  -  |  -  |  -  
        #  _____|_____|_____
        #       |     |     
        # 2  -  |  -  |  -  
        #  _____|_____|_____
        #       |     |     
        # 3  X  |  X  |  X  
        #       |     |     


    elif (logicBoard[0][0] == logicBoard[1][0] == logicBoard[2][0]) and (logicBoard[0][0] != '-'):
        print("You win, %s" % logicBoard[0][0])
        return True

        #    a     b     c
        #       |     |     
        # 1  X  |  -  |  -  
        #  _____|_____|_____
        #       |     |     
        # 2  X  |  -  |  -  
        #  _____|_____|_____
        #       |     |     
        # 3  X  |  -  |  -  
        #       |     |     


    elif (logicBoard[0][1] == logicBoard[1][1] == logicBoard[2][1]) and (logicBoard[0][1] != '-'):
        print("You win, %s" % logicBoard[0][1])
        return True

        #    a     b     c
        #       |     |     
        # 1  -  |  X  |  -  
        #  _____|_____|_____
        #       |     |     
        # 2  -  |  X  |  -  
        #  _____|_____|_____
        #       |     |     
        # 3  -  |  X  |  -  
        #       |     |     


    elif (logicBoard[0][2] == logicBoard[1][2] == logicBoard[2][2]) and (logicBoard[0][2] != '-'):
        print("You win, %s" % logicBoard[0][2])
        return True

        #    a     b     c
        #       |     |     
        # 1  -  |  -  |  X  
        #  _____|_____|_____
        #       |     |     
        # 2  -  |  -  |  X  
        #  _____|_____|_____
        #       |     |     
        # 3  -  |  -  |  X  
        #       |     |     


    elif (logicBoard[0][0] == logicBoard[1][1] == logicBoard[2][2]) and (logicBoard[0][0] != '-'):
        print("You win, %s" % logicBoard[0][0])
        return True

        #    a     b     c
        #       |     |     
        # 1  X  |  -  |  -  
        #  _____|_____|_____
        #       |     |     
        # 2  -  |  X  |  -  
        #  _____|_____|_____
        #       |     |     
        # 3  -  |  -  |  X  
        #       |     |     


    elif (logicBoard[0][2] == logicBoard[1][1] == logicBoard[2][0]) and (logicBoard[0][2] != '-'):
        print("You win, %s" % logicBoard[0][2])
        return True

        #    a     b     c
        #       |     |     
        # 1  -  |  -  |  X  
        #  _____|_____|_____
        #       |     |     
        # 2  -  |  X  |  -  
        #  _____|_____|_____
        #       |     |     
        # 3  X  |  -  |  -  
        #       |     |     
    
    elif not any('-' in x for x in logicBoard): #If there's no empty spaces in the board, it's a tie.
        print("It's a tie!")
        return True

    else:
        return False


def main():
    blankBoard() #Change all cells to be empty to start/restart the game
    turnOrder = whoStarts() #Player choses which sign to be
    playerSign = turnOrder[0] #turn order is an array type where the first value is the player's chosen sign
    computerSign = turnOrder[1]
    i = random.randint(0, 1)       
    print("'%s' starts: " % turnOrder[i]) #Random choose who starts the game
    print(currentBoard())
    while running: 
        if turnOrder[i] == playerSign: #If its the players turn:
            squareValue = playerMove()
        elif turnOrder[i] == computerSign: #If its the machines turn:
            squareValue = computerMove()

        

        logicBoard[squareValue[0]][squareValue[1]] = turnOrder[i] #Change the chosen cell to be the current player/machine sign
        print(currentBoard())
        
        if checkWin():
            break

        if i == 0: #Change turn
            i = 1
        elif i == 1:
            i = 0
        
        print("Your turn '%s': " % turnOrder[i])



if (__name__ == '__main__'):
    playing = True
    while playing:
        main()
        playAgain = input("Another round? y/n: ").lower()

        if playAgain != 'y':
            playing = False