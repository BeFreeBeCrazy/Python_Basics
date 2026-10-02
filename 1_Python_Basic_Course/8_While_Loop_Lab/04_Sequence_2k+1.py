number = int(input())

sum_numbers = 1

while True:
    if sum_numbers <= number:
        print(sum_numbers)
        sum_numbers = sum_numbers * 2 + 1
    else:
        break
        