budget = int(input())

total_price = 0

while True:
    price = input()
    if price != "End":
        price = float(price)
        total_price += price
        if total_price > budget:
            print("You went in overdraft!")
            break
        continue

    else:
        print("You bought everything needed.")
        break