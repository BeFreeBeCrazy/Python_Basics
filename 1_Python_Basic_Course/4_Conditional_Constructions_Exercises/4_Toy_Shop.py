puzzle = 2.60
talking_doll = 3
fluffy_bear = 4.10
minion = 8.20
bus = 2


excursion_price = float(input())
puzzle_quantity = int(input())
talking_doll_quantity = int(input())
fluffy_bear_quantity = int(input())
minion_quantity = int(input())
bus_quantity = int(input())

toys_quantity = puzzle_quantity + talking_doll_quantity + fluffy_bear_quantity + minion_quantity + bus_quantity

puzzle_price = puzzle * puzzle_quantity
talking_doll_price = talking_doll * talking_doll_quantity
fluffy_bear_price = fluffy_bear * fluffy_bear_quantity
minion_price = minion * minion_quantity
bus_price = bus * bus_quantity

total_toy_price = puzzle_price + talking_doll_price + fluffy_bear_price + minion_price + bus_price



if toys_quantity >= 50:
    toy_price_after_discount = total_toy_price * 0.75
    profit_after_rent = toy_price_after_discount * 0.90
else:
    profit_after_rent = total_toy_price * 0.90

profit_after_excursion = profit_after_rent - excursion_price

if profit_after_excursion >= 0:
    print(f'Yes! {profit_after_excursion:.2f} lv left.')
else:
    print(f'Not enough money! {profit_after_excursion * -1:.2f} lv needed.')