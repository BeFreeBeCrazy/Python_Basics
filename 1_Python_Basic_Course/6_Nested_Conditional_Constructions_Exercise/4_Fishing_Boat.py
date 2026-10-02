budget = int(input())
season = str(input())
fishermen = int(input())

discount = 0.0
after_discount = 0.0
money_left = 0.0
boat_price = 0.0

if season == 'Spring':
    boat_price = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_price = 4200
elif season == 'Winter':
    boat_price = 2600

if fishermen <= 6:
    discount = 0.10
elif fishermen <= 11:
    discount = 0.15
elif fishermen > 12:
    discount = 0.25

after_discount = boat_price - (boat_price * discount)

if fishermen % 2 == 0 and season != 'Autumn':
    after_discount = after_discount * 0.95


money_left = budget - after_discount


if money_left >= 0:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_left * -1:.2f} leva.")