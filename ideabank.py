import sys
tablica = []

def readfile():

    with open('plik.txt') as f:
        for line in f:
            tablica.append(line.split(" "))
    return tablica

file_open = open("plik.txt", "a")


if __name__ == "__main__":
    if sys.argv[1] == "add":
        file_open.write("add\n")
    elif sys.argv[1] == "delete":
        file_open.write("delete\n")




