movie_budget = float(input())
statists_number = float(input())
clothes_price = float(input())

total_clothes_price = statists_number * clothes_price

if statists_number >= 150:
    total_clothes_price *= 0.90

decoration = movie_budget * 0.10
money_after_budget =  movie_budget - (decoration + total_clothes_price)

if decoration + total_clothes_price <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {money_after_budget:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {money_after_budget * -1:.2f} leva more.")