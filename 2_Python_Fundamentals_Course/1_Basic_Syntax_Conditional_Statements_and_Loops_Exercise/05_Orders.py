number_of_orders = int(input())

total_price = 0.0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    quantity_capsules = int(input())
    if 0.01 > price_per_capsule or price_per_capsule > 100.00:
        continue
    elif 1 > days or days > 31:
        continue
    elif 1 > quantity_capsules or quantity_capsules > 2000:
        continue
    price = price_per_capsule * quantity_capsules * days
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price

print(f"Total: ${total_price:.2f}")

