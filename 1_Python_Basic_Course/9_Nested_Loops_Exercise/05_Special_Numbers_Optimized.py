number = int(input())

count = 0

for digit in range(1111, 9999 + 1):
    y = str(digit)
    for char in y:
        integer = int(char)
        if integer == 0 or number % integer != 0:
            count = 0
            continue
        elif number % integer == 0:
            count += 1
            if count == 4:
                print(digit, end = " ")
                count = 0
            else:
                continue