
def cat(command):
    with open("files/{}".format(command[1]), "r") as file:
        for line in file:
            print(line)
    