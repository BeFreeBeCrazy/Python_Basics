budget = int(input())
season = str(input())
fishermen = int(input())
price = 0.0

if season == "Spring":
    price = 3000
elif season == "Autumn" or season == "Summer":
    price = 4200
elif season == "Winter":
    price = 2600
if fishermen <= 6:
    price *= 0.9
elif 7 <= fishermen <= 11:
    price *= 0.85
elif fishermen >= 12:
    price *= 0.75
if fishermen % 2 == 0 and season != "Autumn":
    price *= 0.95

calculations = budget - price

if budget >= price:
    print(f"Yes! You have {calculations:.2f} leva left.")
else:
    print(f"Not enough money! You need {(calculations * -1):.2f} leva.")
