import sys

number = input()

min_number = sys.maxsize

while number != "Stop":
    actual_number = int(number)
    if actual_number < min_number:
        min_number = actual_number
        number = input()
    else:
        number = input()

print(min_number)