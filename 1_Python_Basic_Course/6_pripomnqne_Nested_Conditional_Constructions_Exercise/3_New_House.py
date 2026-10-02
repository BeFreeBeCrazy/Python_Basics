flowers_type = str(input())
number_flowers = int(input())
budget = float(input())
discount = 0.0
price = 0

if flowers_type == "Roses":
    price = 5
    if number_flowers > 80:
        price *= 0.9
elif flowers_type == "Dahlias":
    price = 3.80
    if number_flowers > 90:
        price *= 0.85
elif flowers_type == "Tulips":
    price = 2.80
    if number_flowers > 80:
        price *= 0.85
elif flowers_type == "Narcissus":
    price = 3
    if number_flowers < 120:
        price *= 1.15
elif flowers_type == "Gladiolus":
    price = 2.50
    if number_flowers < 80:
        price *= 1.20

bill = price * number_flowers

difference = budget - bill

if budget >= bill:
    print(f"Hey, you have a great garden with {number_flowers} {flowers_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {(difference * -1):.2f} leva more.")


