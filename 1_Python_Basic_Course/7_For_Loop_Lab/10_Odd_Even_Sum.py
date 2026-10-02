n = int(input())
even_sum = 0
odd_sum = 0


for idx in range(n):
    numbers = int(input())
    if idx % 2 == 0:
        even_sum += numbers
    else:
        odd_sum += numbers

calculation = even_sum - odd_sum

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {abs(calculation)}")
