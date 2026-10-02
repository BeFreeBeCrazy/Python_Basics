budget = float(input())
overnight_stay = int(input())
price_overnight_stay = float(input())
percentage_additional_expenses = int(input())

percentage_additional_expenses /= 100

if overnight_stay > 7:
    price_overnight_stay *= 0.95

overall_price = price_overnight_stay * overnight_stay + (budget * percentage_additional_expenses)

if budget >= overall_price:
    print(f"Ivanovi will be left with {budget - overall_price:.2f} leva after vacation.")
else:
    print(f"{overall_price - budget:.2f} leva needed.")