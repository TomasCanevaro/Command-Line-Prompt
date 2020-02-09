
def sort(command):
    with open("files/{}".format(command[1]), "r") as file:
        sorted_lines = []
        for line in file:
            sorted_lines.append(line)
        sorted_lines.sort()
        for sl in sorted_lines:
            print(sl)