budget = float(input())
season = str(input())

destination = ''
money_spent = 0.0
accomodation = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        accomodation = 'Camp'
        money_spent = budget * 0.30
    elif season == 'winter':
        accomodation = 'Hotel'
        money_spent = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        accomodation = 'Camp'
        money_spent = budget * 0.40
    elif season == 'winter':
        accomodation = 'Hotel'
        money_spent = budget * 0.80
elif budget > 1000:
    destination = 'Europe'
    if season == 'summer':
        accomodation = 'Hotel'
        money_spent = budget * 0.90
    elif season == 'winter':
        accomodation = 'Hotel'
        money_spent = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{accomodation} - {money_spent:.2f}")