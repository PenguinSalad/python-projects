#!/usr/bin/env python3

def bookFunc(bookAmount):
    if bookAmount == 1: bookTotal = 3
    elif bookAmount == 2: bookTotal = 5
    elif bookAmount == 3: bookTotal = 8
    elif bookAmount == 4 or bookAmount == 5: bookTotal = 10
    elif bookAmount == 6: bookTotal = 13
    elif bookAmount == 7: bookTotal = 15
    elif bookAmount == 8: bookTotal = 18
    elif bookAmount == 9 or bookAmount == 10: bookTotal = 20
    else:
        bookTotal = eval(input("Per quin preu total?: "))
    return bookTotal
def othersFunc():
    othersTotal = eval(input("Quin preu?: "))
    return othersTotal


#Definim llistes de possibles inputs#################################################################
book = ["book","llibre","b","l"]
altres = ["others","other","altre","altres"]
done = ["done","quit","exit","d","q","e"]
cash = ["cash","efectiu","c"]
credit = ["credit","card"]
#####################################################################################################

changeBack = True

while True:
    itemType = input("Tipus de item: ")
    if itemType.lower() in book:
        bookAmount = eval(input("Quina quantitat: "))
        bookTotal = bookFunc(bookAmount)
    elif itemType.lower() in altres:
        othersTotal = othersFunc()
    elif itemType.lower() in done:
        try:
            bookTotal
        except NameError:
            bookTotal = 0
        try:
            othersTotal
        except NameError:
            othersTotal = 0
        costTotal = bookTotal + othersTotal
        break
    else:
        print("Not a registered answer")
print("En total seran %d€" % costTotal)
payMethod = input("Cash or credit card? ")
while True:
    if payMethod in cash:
        while changeBack:
            cashAmount = eval(input("Em donen: "))
            returnAmount = cashAmount - costTotal
            if returnAmount >= 0:
                print ("Torna %d€ de canvi" % returnAmount)
                print("\nPrint ticket")
                print("\nOpen register")
                changeBack = False
                break
            else:
                print("Quantitat entregada es menor que el cost total")
    elif payMethod in credit:
        print("\nPrint ticket ")
        break
