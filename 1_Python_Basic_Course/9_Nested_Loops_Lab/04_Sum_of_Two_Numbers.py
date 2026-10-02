number1 = int(input())
number2 = int(input())
magic_number = int(input())

combinations_count = 0
calculations = 0
found = False

# while found != True:
for x1 in range(number1, number2 + 1):
    for x2 in range(number1, number2 + 1):
        combinations_count += 1
        if (x1 + x2) == magic_number:
            found = True
            print(f"Combination N:{combinations_count} ({x1} + {x2} = {magic_number})")
            break
    if found:
        break

if not found:
    print(f"{combinations_count} combinations - neither equals {magic_number}")

