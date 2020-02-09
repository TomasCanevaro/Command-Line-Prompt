from functions.cat import cat
from functions.sort import sort

while(True):
    #Fist thing, i take the command and decompose it
    command = input("$ ")
    command = command.split(" ")

    #Then, i check for the function
    if(command[0] == "cat"):
        cat(command)
    if(command[0] == "sort"):
        sort(command)
    if(command[0] == "end"):
        break