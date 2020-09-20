def return_gedanken():
    if len(thoughts) == 0:
        return ("Du hast noch keine Gedanken gespeichert!")
    else:
        return (thoughts[0:])

thoughts = ["Gedanke", "2. Gedanke"]

running = True

def quit_program():
    exit(0)

def print_help():
    print(Commands.keys())

def print_thoughts():
    pass

def write():
    pass

def load():
    pass
Commands = {
    'help': print_help,
    'quit': quit_program,
    'thoughts': print_thoughts,
    'write': write,
    'load': load
}

if __name__ == '__main__':
    print("Thought Memory")
    while True:
        command = input("> ").lower().split(" ")
        if command[0] in Commands:
            if len(command) > 1:
                Commands[command[0]](command[:])
            else:
                Commands[command[0]]()
        else:
            print("Unknown command")

