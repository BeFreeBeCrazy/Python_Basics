money = input()

sum_money = 0

while money != "NoMoreMoney":
    increased_money = float(money)
    if increased_money >= 0:
        sum_money += increased_money
        print(f"Increase: {increased_money:.2f}")
        money = input()
    else:
        print("Invalid operation!")
        break

print(f"Total: {sum_money:.2f}")