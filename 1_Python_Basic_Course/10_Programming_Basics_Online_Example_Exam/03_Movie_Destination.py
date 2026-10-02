budget = float(input())
destination = str(input())
season = str(input())
days = int(input())

price = 0

if season == "Winter":

    if destination == "Dubai":
        price = 45_000 * 0.7
    elif destination == "Sofia":
        price = 17_000 * 1.25
    elif destination == "London":
        price = 24_000

elif season == "Summer":
    if destination == "Dubai":
        price = 40_000 * 0.7
    elif destination == "Sofia":
        price = 12_500 * 1.25
    elif destination == "London":
        price = 20_250

expenses = price * days

if budget >= expenses:
    print(f"The budget for the movie is enough! We have {budget - expenses:.2f} leva left!")
else:
    print(f"The director needs {expenses - budget:.2f} leva more!")