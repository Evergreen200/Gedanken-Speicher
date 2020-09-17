def return_gedanken():
  if len(thoughts) == 0:
    return("Du hast noch keine Gedanken gespeichert!")
  else:
    return(thought[0:])
   
def commands():
  command_list = ["gedanken"]
  return(command_list[0:])
 
print("Thought Memory")

thoughts = ["Gedanke", "2. Gedanke"]

if (input() == "gedanken"):
  print(return_gedanken())
  
if (input() == "commands" or "help"):
  print(commands())
