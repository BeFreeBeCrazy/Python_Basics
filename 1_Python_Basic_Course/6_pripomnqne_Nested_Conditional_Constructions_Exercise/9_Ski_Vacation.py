days = int(input())
room_type = str(input())
review = str(input())
discount = 0.0
nights = days - 1
price = 0.0

if room_type == "room for one person":
    price = 18.00
    if days < 10:
        discount = 0
    elif 10 <= days <= 15:
        discount = 0
    elif days > 15:
        discount = 0
elif room_type == "apartment":
    price = 25.00
    if days < 10:
        discount = 0.30
    elif 10 <= days <= 15:
        discount = 0.35
    elif days > 15:
        discount = 0.50
elif room_type == "president apartment":
    price = 35.00
    if days < 10:
        discount = 0.10
    elif 10 <= days <= 15:
        discount = 0.15
    elif days > 15:
        discount = 0.20

if discount != 0:
    bill = (nights * price) - (nights * price * discount)
elif discount == 0:
    bill = nights * price

if review == "positive":
    bill *= 1.25
elif review == "negative":
    bill *= 0.90


print(f"{bill:.2f}")
