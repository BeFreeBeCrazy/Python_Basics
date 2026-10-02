numbers = int(input())

for _ in range(1, numbers + 1):
    integer = int(input())
    if integer % 2 != 0:
        print(integer, "is odd!")
        break

else:
    print("All numbers are even.")