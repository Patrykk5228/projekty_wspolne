import sys

add_list = []
delete_list = []

def add_idea():
    with open('plik.txt') as f:
        for line in f:
            add_list.append(line.split(" "))
    return add_list

def remove_idea():
    with open('plik.txt') as f:
        for line in f:
            for idea in delete_list:
                line = line.replace(idea, "")
    return f.write(line)
        

file_open = open("plik.txt", "a")

idea = sys.argv[2]

if __name__ == "__main__":
    if sys.argv[1] == "add" and len(sys.argv[2]) > 0:
        file_open.write(idea + "\n")
    elif sys.argv[1] == "delete":
        remove_idea("delete\n")
delete_list = []
