import sys

number = input()

max_number = -sys.maxsize

while number != "Stop":
    actual_numbers = int(number)
    if actual_numbers > max_number:
        max_number = actual_numbers
        number = input()
    else:
        number = input()

print(max_number)