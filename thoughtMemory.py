import sys

def return_gedanken():
    if len(thoughts) == 0:
        return("Du hast noch keine Gedanken gespeichert!")
    else:
        return(thoughts[0:])

def commands():
    command_list = ["gedanken"] # later, i will rename all functions and commands
    return(command_list[0:])

def quit():
    running = False
    sys.exit()

thoughts = ["Gedanke", "2. Gedanke"]

running = True

if __name__ == '__main__':
    print("Thought Memory") 
    # while running:

    if input() == "gedanken":
        print(return_gedanken())
    elif input() == "commands" or "help":
        print(commands()) 
    elif input() == "exit":
        quit()

            