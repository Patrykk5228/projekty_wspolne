import readline
import sys
import os

def is_string(userInput):
    if userInput.isdigit() is False:
        return True
    return False

def load_idea():
    with open('File.txt') as f:
        line = f.readline()
        load_list.append(line)
    return load_list

def save_idea():
    file = open("File.txt","w")
    file.write(idea)
    file.close()
        

def remove_idea():
    with open('File.txt') as f:
        for line in f:
            for idea in delete_list:
                line = line.replace(idea, "")
                return f.write(line)
    
def ask_for_idea(force_valid_input):
    while True:
        idea = input("\nWhat is your new idea?")
        isString = is_string(idea)
        if isString is False:
            if not force_valid_input:
                return None
            print("Not a correct sentence.")
        else:
            return idea

load_list = []
delete_list = []
load_idea()
while True:
    try:
        idea = ask_for_idea(True)
        load_list.append(idea)
        for i, item in enumerate(load_list,1):
            print(i, '. ' + item, sep='',end='' + "\n")
        save_idea()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
"""
if __name__ == "__main__":
    idea = sys.argv[2]
    if sys.argv[1] == "add" and len(sys.argv[2]) > 0:
        file_open.write(idea + "\n")
    elif sys.argv[1] == "delete" and len(sys.argv[2]) > 0:
        remove_idea()
"""
