number = int(input())

combinations_count = 0

for number1 in range(number + 1):
    for number2 in range(number + 1):
        for number3 in range(number + 1):
            if number1 + number2 + number3 == number:
                combinations_count += 1
            if number1 == number:
                break
print(combinations_count)