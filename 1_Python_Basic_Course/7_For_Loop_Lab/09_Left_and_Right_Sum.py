n = int(input())
left_sum = right_sum = 0
calculation = 0

for idx in range(2 * n):
    numbers = int(input())
    if idx < n:
        left_sum += numbers
    else:
        right_sum += numbers

calculation = left_sum - right_sum

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(calculation)}")
