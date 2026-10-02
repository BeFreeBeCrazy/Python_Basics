flowers = str(input())
quantity = int(input())
budget = float(input())

rose = 5 * quantity
dahlia = 3.80 * quantity
tulip = 2.80 * quantity
narcissus = 3 * quantity
gladiolus = 2.50 * quantity

discount = 0

if flowers == 'Roses' and quantity > 80:
    discount = 0.10
elif flowers == 'Dahlias' and quantity > 90:
    discount = 0.15
elif flowers == 'Tulips' and quantity > 80:
    discount = 0.15
elif flowers == 'Narcissus' and quantity < 120:
    discount = 0.15
elif flowers == 'Gladiolus' and quantity < 80:
    discount = 0.20

if flowers == 'Roses':
    total_price = rose - (rose * discount)
elif flowers == 'Dahlias':
    total_price = dahlia - (dahlia * discount)
elif flowers == 'Tulips':
    total_price = tulip - (tulip * discount)
elif flowers == 'Narcissus':
    total_price = narcissus + (narcissus * discount)
elif flowers == 'Gladiolus':
    total_price = gladiolus + (gladiolus * discount)

money_left = budget - total_price

if money_left >= 0:
    print (f"Hey, you have a great garden with {quantity} {flowers} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_left * -1:.2f} leva more.")