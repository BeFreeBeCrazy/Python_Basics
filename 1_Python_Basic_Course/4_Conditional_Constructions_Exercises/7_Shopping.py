peter_budget = float(input())
videocards_number = int(input())
cpu_number = int(input())
ram_number = int(input())

videocards_price = videocards_number * 250
cpu_price = videocards_price * 0.35 * cpu_number
ram_price = videocards_price * 0.10 * ram_number

total_price = videocards_price + cpu_price + ram_price

if videocards_number > cpu_number:
    total_price *= 0.85

final_calculations = peter_budget - total_price

if peter_budget >= total_price:
    print(f"You have {final_calculations:.2f} leva left!")
else:
    print(f"Not enough money! You need {final_calculations * -1:.2f} leva more!")