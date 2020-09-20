import json
# TODO: Implement json, delete function

def quit_program():
    exit(0)

def print_help():
    print(Commands.keys())

def print_thoughts():
    with open('data.json') as file:
        data = json.load(file)
#   print(json.dumps(data["thoughts"], indent=4))

    for thoughts in data['thoughts']:
        print(thoughts['name'], thoughts['content'])

def new_thought():
    with open('data.json') as file:
        data = json.load(file)

    thought_name_ui = input("Dein Gedanke: ")
    thought_content_ui = input("Inhalt: ")

    list = [{"name": "Name", "content": "Inhalt"}]
    data['thoughts'].extend(list)

#   print(data['thoughts'][-1]) -> to check if the element was added

    data['thoughts'][-1] = {'name': thought_name_ui, 'content': thought_content_ui}

    with open('data.json', 'w') as fout:
        fout.write(json.dumps(data, indent=4))


Commands = {
    'help': print_help,
    'quit': quit_program,
    'thoughts': print_thoughts, # thoughts.thought1 for specific thought
    'new': new_thought
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

