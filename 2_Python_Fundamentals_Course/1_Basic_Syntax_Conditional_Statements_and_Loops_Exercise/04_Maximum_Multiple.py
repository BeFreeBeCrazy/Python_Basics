divisor = int(input())
boundary = int(input())

for _ in range(boundary, 1, -1):
    if _ % divisor == 0:
        print(_)
        break
    else:
        continue