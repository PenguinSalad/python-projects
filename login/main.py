#!/usr/bin/env python3
import time
from hashlib import blake2b
from hmac import compare_digest

def welcome():
    print ("-"*75)
    print ("\n                     Welcome to penguinSalad.com\n")
    print ("-"*75)
    time.sleep(1)
    print ("\nWould you like to LOGIN or REGISTER?\n")

main = True
wrongPass = 0
#Main while loop
while main:
    #Welcome message
    welcome()
    asking = True
    access = False
    while asking:
        regorLog = input('"Press l for Login, r for Register" ')
        if (regorLog == "r") or (regorLog == "R"):
        #If Register
            #Ask for username and password
            #Username loop
            #If username already exists, ask for another one
            username = input("user: ").encode('utf-8')
            #Make the user repeat the password
            while True:
                password = input("password: ").encode('utf-8')
                repPass = input("Please repeat your password: ").encode('utf-8')
                if (password == repPass):
                    userInfo = blake2b(digest_size=20)
                    userInfo.update(b"%s-%s" % (username, password))
                    #Open users file
                    usersFile = open('users.txt', 'a')
                    usersFile.write(userInfo.hexdigest()) #Store the hashed userInfo
                    usersFile.write("\n")
                    usersFile.close()
                    #User created!
                    print("\nUser %s created successfuly! Going back to menu...\n" % username)
                    time.sleep(1)
                    break
                else:
                    print("Passwords don't match, please try again")
            asking = False
        elif (regorLog == "l") or (regorLog == "L"):
        #Elif Login
            #Ask for the username and password
            logUser = input("Username: ").encode('utf-8')
            logPass = input("Password: ").encode('utf-8')
            #Hashes the login info
            loginInfo = blake2b(digest_size=20)
            loginInfo.update(b"%s-%s" % (logUser, logPass))
            #Reads the users.txt file, line per line
            with open("users.txt") as usersfile:
                readLine = usersfile.readlines()
            for x in range(len(readLine)):
                #If one of the lines contains the same hash as the one used for login:
                if (loginInfo.hexdigest() == readLine[x].rstrip()):
                    #Grants access
                    access = True
                    break
            else: #If the hash doesn't exist
                print("Wrong username or password\n")
        else: #In case they don't write either L or R
            print("That's not a valid answer\n")

        if access: #If the user and password match
            print("I'm in")
            main = False
            asking = False
