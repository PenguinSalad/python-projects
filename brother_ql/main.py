#!/usr/bin/env python3

def bookFunc(bookAmount):
    if bookAmount == 1:
        bookTotal = 3
        return bookTotal
    elif bookAmount == 2:
        bookTotal = 5
        return bookTotal
    elif bookAmount == 3:
        bookTotal = 8
        return bookTotal
    elif bookAmount == 4 or bookAmount == 5:
        bookTotal = 10
        return bookTotal
    elif bookAmount == 6:
        bookTotal = 13
        return bookTotal
    elif bookAmount == 7:
        bookTotal = 15
        return bookTotal
    elif bookAmount == 8:
        bookTotal = 18
        return bookTotal
    elif bookAmount == 9 or bookAmount == 10:
        bookTotal = 20
        return bookTotal
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
        cashAmount = eval(input("Em donen: "))
        returnAmount = cashAmount - costTotal
        print ("Torna %d€ de canvi" % returnAmount)
        print("\nPrint ticket")
        print("\nOpen register")
        break
    elif payMethod in credit:
        print("\nPrint ticke ")
        break
