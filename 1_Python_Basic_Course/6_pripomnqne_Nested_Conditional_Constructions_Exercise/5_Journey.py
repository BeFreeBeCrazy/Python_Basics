budget = float(input())
season = str(input())
destination = ""
expenses = 0.0
vacation_type = ""

if 100 >= budget:
    destination = "Bulgaria"
    if season == "summer":
        expenses = budget * 0.3
        vacation_type = "Camp"
    elif season == "winter":
        expenses = budget * 0.7
        vacation_type = "Hotel"
elif 1000 >= budget:
    destination = "Balkans"
    if season == "summer":
        expenses = budget * 0.4
        vacation_type = "Camp"
    elif season == "winter":
        expenses = budget * 0.8
        vacation_type = "Hotel"
elif 1000 < budget:
    destination = "Europe"
    expenses = budget * 0.9
    vacation_type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{vacation_type} - {expenses:.2f}")