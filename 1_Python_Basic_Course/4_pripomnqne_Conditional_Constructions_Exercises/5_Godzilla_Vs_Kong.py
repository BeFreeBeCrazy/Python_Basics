movie_budget = float(input())
statists_number = float(input())
clothes_price = float(input())

decor = movie_budget * 0.1

if statists_number > 150:
    clothes_price = clothes_price - clothes_price * 0.1

total_expenses = statists_number * clothes_price
last_calculations = movie_budget - total_expenses - decor

if last_calculations < 0:
    print ("Not enough money!")
    print (f"Wingard needs {(last_calculations * -1):.2f} leva more.")
elif last_calculations >= 0:
    print ("Action!")
    print (f"Wingard starts filming with {last_calculations:.2f} leva left.")