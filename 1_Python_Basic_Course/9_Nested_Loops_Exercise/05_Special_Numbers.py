number = int(input())

count = 0

for digit in range(1111, 9999 + 1):
    y = str(digit)
    for char in y:
        count += 1
        integer = int(char)
        if int(y[0]) == 0 or int(y[1]) == 0 or int(y[2]) == 0 or int(y[3]) == 0:
            continue
        if number % int(y[0]) == 0 and number % int(y[1]) == 0 and number % int(y[2]) == 0 and number % int(y[3]) == 0:
            print(digit, end=" ")
            break
        else:
            break
