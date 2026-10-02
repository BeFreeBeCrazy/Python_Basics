pack_of_pens = 5.80
pack_of_markers = 7.20
liquid = 1.20

number_of_pen_packs = int(input())
number_of_marker_packs = int(input())
litres_of_liquid = int(input())
discount_percent = int(input())

actual_discount = discount_percent / 100

pen_price = number_of_pen_packs * pack_of_pens
marker_price = number_of_marker_packs * pack_of_markers
liquid_price = litres_of_liquid * liquid
total_price = pen_price + marker_price + liquid_price
total_price_after_discount = total_price - (total_price * actual_discount)

print(total_price_after_discount)

