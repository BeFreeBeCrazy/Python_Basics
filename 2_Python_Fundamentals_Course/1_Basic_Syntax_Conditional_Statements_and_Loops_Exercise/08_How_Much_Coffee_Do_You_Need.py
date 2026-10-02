command = str(input())

coffees_needed = 0

while command != "END":
    saving_command = command
    command_lower = (command.lower())
    if (command_lower == "coding" 
        or command_lower == "dog" 
        or command_lower == "cat" 
        or command_lower == "movie"):
        for _ in range(1):
            if saving_command == (command.lower()):
                coffees_needed += 1
            elif saving_command == (command.upper()):
                coffees_needed += 2
    if coffees_needed > 5:
        print("You need extra sleep")
        break
    command = str(input())
    if command == "END":
        print(coffees_needed)

    