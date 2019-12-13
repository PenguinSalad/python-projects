import time


def welcome():
    print ("-"*75)
    print ("\n                     Welcome to penguinSalad.com\n")
    print ("-"*75)
    time.sleep(1)
    print ("\nWould you like to LOGIN or REGISTER?\n")

#Main while loop
while True:
    #Welcome message
    welcome()
    asking = True
    while asking:
        regorLog = input('"Press l for Login, r for Register "')
        if (regorLog == "r") or (regorLog == "R"):
        #If Register
            #Ask for username and password
            #Username loop
            #If username already exists, ask for another one
            username = input("Username: ")
            #Make the user repeat the password
            while True:
                password = input("Password: ")
                repPass = input("Please repeat your password: ")
                if (password == repPass):
                    #Store those 2 values in a .txt
                    print("\nUser %s created successfuly! Going back to menu...\n" % username)
                    time.sleep(2.5)
                    user = ("%s - %s\n" % (username, password))
                    with open("users.txt", "a") as usersfile:
                        usersfile.write(user)
                        usersfile.close()
                    break
                else:
                    print("Passwords don't match, please try again")
            asking = False



        elif (regorLog == "l") or (regorLog == "L"):
        #Elif Login
            #Ask for the username and password
            logUser = input("Username: ")
            #Checks if the username exists
            #Checks if the password matches the username selected
            logPass = input("Password: ")
            #Gets access
            asking = False

        else:
            print("That's not a valid answer\n")
