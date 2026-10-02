strawb_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberry_quantity = float(input())
strawb_quantity = float(input())

raspberry_price = strawb_price * 0.5
oranges_price = raspberry_price * 0.6
bananas_price = raspberry_price * 0.2


bananas_price *= bananas_quantity
strawb_price *= strawb_quantity
oranges_price *= oranges_quantity
raspberry_price *= raspberry_quantity

needed_money = bananas_price + strawb_price + oranges_price + raspberry_price

print(f"{needed_money:.2f}")