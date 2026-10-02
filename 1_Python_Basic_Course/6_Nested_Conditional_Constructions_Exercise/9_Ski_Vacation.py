days = int(input())
room_type = str(input())
grade = str(input())

nights = days - 1
total_price = 0

if room_type == 'room for one person':
    room = 18
    if nights < 10:
        discount = 0
    elif nights <= 15:
        discount = 0
    elif nights > 15:
        discount = 0
elif room_type == 'apartment':
    room = 25
    if nights < 10:
        discount = 0.30
    elif nights <= 15:
        discount = 0.35
    elif nights > 15:
        discount = 0.50
elif room_type == 'president apartment':
    room = 35
    if nights < 10:
        discount = 0.10
    elif nights <= 15:
        discount = 0.15
    elif nights > 15:
        discount = 0.20

price_after_discount = (nights * room) - (nights * room * discount)

if discount <= 0:
    price_after_discount = nights * room

if grade == 'positive':
    price_after_discount = price_after_discount * 1.25
elif grade == 'negative':
    price_after_discount = price_after_discount * 0.90

print(f"{price_after_discount:.2f}")