#!/usr/bin/env python3

with open("users.txt") as usersfile:
    user = input(": ")
    readLine = usersfile.readlines()

    for x in range(len(readLine)):
        if (user == readLine[x].split("-")[0]):
            print("Ok")
        else:
            print("No")
