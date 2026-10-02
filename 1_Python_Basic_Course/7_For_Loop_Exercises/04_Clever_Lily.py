lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

saved_money = 0
toys = 0

for birthday in range(1, lily_age + 1):
    if birthday % 2 == 0:
        birthday_savings = birthday * 10 / 2
        saved_money += birthday_savings - 1

    else:
        toys += 1

calculations_toys = toys * toy_price
total_savings = calculations_toys + saved_money

if total_savings - washing_machine_price >= 0:
    print(f"Yes! {total_savings - washing_machine_price:.2f}")
else:
    print(f"No! {abs(washing_machine_price - total_savings):.2f}")