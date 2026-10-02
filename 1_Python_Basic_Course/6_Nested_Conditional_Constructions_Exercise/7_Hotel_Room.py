month = str(input())
nights = int(input())

studio = 0.0
apartment = 0.0
discount_studio = 0.0
discount_apartment = 0.0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if 14 > nights > 7:
        discount_studio = 0.95 * studio
    elif nights > 14:
        discount_studio = 0.70 * studio
elif month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        discount_studio = 0.80 * studio
elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77

if nights > 14:
    discount_apartment = 0.90 * apartment

if discount_apartment == 0:
    total_price_apartment = nights * apartment
else:
    total_price_apartment = nights * discount_apartment

if discount_studio == 0:
    total_price_studio = nights * studio
else:
    total_price_studio = nights * discount_studio


print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")