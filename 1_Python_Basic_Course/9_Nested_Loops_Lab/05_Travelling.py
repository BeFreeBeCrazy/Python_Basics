destination = str(input())
needed_money = float(input())

saved_money = 0

while destination != "End":
    dest = str(destination)
    while True:
        money = float(input())
        saved_money += money
        if saved_money >= needed_money:
            print(f"Going to {destination}!")
            destination = str(input())
            if destination != "End":
                needed_money = float(input())
            saved_money = 0
            break