puzzle = 2.60
talking_doll = 3
teddy_bear = 4.10
minion = 8.20
small_trucky_truck = 2

price_of_excursion = float(input())
puzzle_quantity = int(input())
talking_doll_quantity = int(input())
teddy_bear_quantity = int(input())
minion_quantity = int(input())
small_trucky_truck_quantity = int(input())

pozzle_price = puzzle * puzzle_quantity
tolking_doll_price = talking_doll * talking_doll_quantity
todka_bear_price = teddy_bear * teddy_bear_quantity
menion_price = minion * minion_quantity
smoll_trucky_truck_price = small_trucky_truck * small_trucky_truck_quantity

totalka_price = pozzle_price + tolking_doll_price + todka_bear_price + menion_price + smoll_trucky_truck_price

total_quantity = puzzle_quantity + talking_doll_quantity + teddy_bear_quantity + minion_quantity + small_trucky_truck_quantity

if total_quantity >= 50:
    totalka_price = totalka_price - totalka_price * 0.25

totalka_price = totalka_price - totalka_price * 0.1

last_calculations = totalka_price - price_of_excursion

if last_calculations >= 0:
    print (f"Yes! {last_calculations:.2f} lv left.")
elif last_calculations < 0:
    print (f"Not enough money! {(last_calculations * -1):.2f} lv needed.")