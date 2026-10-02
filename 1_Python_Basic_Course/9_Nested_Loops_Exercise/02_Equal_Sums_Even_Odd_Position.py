number1 = int(input())
number2 = int(input())

odd = ""
even = ""

for x in range(number1, number2 + 1):
    for y in range(x, x + 1):
        pass
    y = str(y)
    odd1 = y[0]
    odd2 = y[2]
    odd3 = y[4]
    even1 = y[1]
    even2 = y[3]
    even3 = y[5]
    summed_odds = int(odd1) + int(odd2) + int(odd3)
    summed_evens = int(even1) + int(even2) + int(even3)

    if summed_odds == summed_evens:
        print ((y), end= " ")