import sys
tablica = []

def readfile():

    with open('plik.txt') as f:
        for line in f:
            tablica.append(line.split(" "))
    return tablica

f = open("plik.txt", "w")




if __name__ == "__main__":
    print(sys.argv)
    if sys.argv[1] == "add":
        print(len(sys.argv))
        f.write("add")


print(len(sys.argv))
print("Argument List:", str(sys.argv))



