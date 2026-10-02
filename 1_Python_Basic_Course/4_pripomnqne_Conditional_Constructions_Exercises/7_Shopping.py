Peter_budget = float(input())
video_cards = float(input())
processors = float(input())
memory = float(input())

vodeo_card_price = 250

video_price = video_cards * vodeo_card_price
precossor_price = video_price * 0.35
momery_price = video_price * 0.1
processor_price = processors * precossor_price
memory_price = memory * momery_price

total_price = video_price + processor_price + memory_price

if video_cards > processors:
    total_price = total_price - total_price * 0.15

last_calculations = Peter_budget - total_price

if Peter_budget >= total_price:
    print (f"You have {last_calculations:.2f} leva left!")
elif total_price > Peter_budget:
    print (f"Not enough money! You need {last_calculations * -1:.2f} leva more!")