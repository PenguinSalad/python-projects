import random

from copy import copy, deepcopy

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


def computerMove(logicBoard, computerSign, playerSign):
    ###Random movement:
   
    # while True:
    #     squareValue = [random.randint(0, 2), random.randint(0, 2)]
    #     if logicBoard[squareValue[0]][squareValue[1]] == '-':
    #         break
    # return squareValue


    ###Logical movement:

    # 1. Check if there's a possible winning move:

    for i in range(3):
        for j in range(3): #Loop through the board
            copyBoard = deepcopy(logicBoard)    #Create a copy    
            if copyBoard[i][j] == '-': #If the cell is empty:
                copyBoard[i][j] = computerSign #Place computer sign and check if we win
                if checkWin(copyBoard):
                    squareValue = [i, j] #If it's a winning move, return it
                    print("Winning move")
                    return squareValue

    # 2. Check if it can block a player's winning move:

    for i in range(3):
        for j in range(3): #Loop through the board
            copyBoard = deepcopy(logicBoard) #Create a copy    
            if copyBoard[i][j] == '-': #If the cell is empty:
                copyBoard[i][j] = playerSign #Place player sign and check if we win
                if checkWin(copyBoard):
                    squareValue = [i, j] #If it's a player's winning move, block it
                    print("Block move")
                    return squareValue



    # 3. Check corners

    corners = [[0,0], [0,2], [2,0], [2,2]] #Corner positions in board

    while True:
        chosenCorner = corners[random.randint(0, 3)] #Choose a random corner
        if logicBoard[chosenCorner[0]][chosenCorner[1]] == '-': #Check if it's empty
            print("Corner move")
            return chosenCorner

    # 4. Check center

    if logicBoard[1][1] == '-': #If the center is empty, place there
        squareValue = [1, 1]
        print("Center move")
        return squareValue

    # 5. Check sides

    sides = [[0,1], [1,0], [1,2], [2,1]] #Sides positions in board

    while True:
        chosenSide = sides[random.randint(0, 3)] #Choose a random side
        if logicBoard[chosenSide[0]][chosenSide[1]] == '-': #Check if it's empty
            print("Side move")
            return chosenSide



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


def checkWin(board):

    if (board[0][0] == board[0][1] == board[0][2]) and (board[0][0] != '-'): 
        print("You win, %s" % board[0][0])
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


    elif (board[1][0] == board[1][1] == board[1][2]) and (board[1][0] != '-'):
        print("You win, %s" % board[1][0])
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


    elif (board[2][0] == board[2][1] == board[2][2]) and (board[2][0] != '-'):
        print("You win, %s" % board[2][0])
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


    elif (board[0][0] == board[1][0] == board[2][0]) and (board[0][0] != '-'):
        print("You win, %s" % board[0][0])
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


    elif (board[0][1] == board[1][1] == board[2][1]) and (board[0][1] != '-'):
        print("You win, %s" % board[0][1])
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


    elif (board[0][2] == board[1][2] == board[2][2]) and (board[0][2] != '-'):
        print("You win, %s" % board[0][2])
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


    elif (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != '-'):
        print("You win, %s" % board[0][0])
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


    elif (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != '-'):
        print("You win, %s" % board[0][2])
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
    
    elif not any('-' in x for x in board): #If there's no empty spaces in the board, it's a tie.
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
            squareValue = computerMove(logicBoard,computerSign, playerSign)

        

        logicBoard[squareValue[0]][squareValue[1]] = turnOrder[i] #Change the chosen cell to be the current player/machine sign
        print(currentBoard())
        
        if checkWin(logicBoard):
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