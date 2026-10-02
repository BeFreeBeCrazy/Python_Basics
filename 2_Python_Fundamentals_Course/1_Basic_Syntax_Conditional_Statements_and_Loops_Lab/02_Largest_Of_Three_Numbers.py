import sys
largest_number = -sys.maxsize

for _ in range (1, 4):
    number = int(input())
    if number > largest_number:
        largest_number = number

print(largest_number)