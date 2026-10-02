needed_money = float(input())
current_money = float(input())

saved_money = current_money
bad_days_count = 0
days_count = 0

while needed_money > saved_money:
    action = str(input())
    flow_money = float(input())
    days_count += 1
    if action == "spend":
        bad_days_count += 1
        saved_money -= flow_money
        if saved_money < 0:
            saved_money = 0
    elif action == "save":
        saved_money += flow_money
        bad_days_count = 0
    if bad_days_count == 5:
        print("You can't save the money.")
        print(f"{days_count}")
        break
    if needed_money <= saved_money:
        print(f"You saved the money for {days_count} days.")
        break