import sys
number_count = int(input())
sum_numbers = 0
next_number = -sys.maxsize

for _ in range (number_count):
    given_number = int(input())
    sum_numbers += given_number
    if given_number > next_number:
        next_number = given_number

final_calculation = sum_numbers - next_number

if sum_numbers - next_number == next_number:
    print("Yes")
    print(f"Sum = {next_number}")
else:
    print("No")
    print(f"Diff = {abs(next_number - final_calculation)}")
