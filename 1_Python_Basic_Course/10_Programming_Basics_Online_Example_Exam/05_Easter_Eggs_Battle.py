participant1_eggs = int(input())
participant2_eggs = int(input())

command = str(input())

while True:
    command = str(command)
    if command == "End":
        print(f"Player one has {participant1_eggs} eggs left.")
        print(f"Player two has {participant2_eggs} eggs left.")
        break
    if command == "one":
        participant2_eggs -= 1
    if command == "two":
        participant1_eggs -= 1
    if participant1_eggs == 0:
        print(f"Player one is out of eggs. Player two has {participant2_eggs} eggs left.")
        break
    if participant2_eggs == 0:
        print(f"Player two is out of eggs. Player one has {participant1_eggs} eggs left.")
        break
    command = str(input())