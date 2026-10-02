degrees = int(input())
time_of_day = str(input())

if time_of_day == 'Morning' and 10 <= degrees <= 18:
    outfit = 'Sweatshirt'
    shoes = 'Sneakers'
elif time_of_day == 'Morning' and 18 < degrees <= 24:
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif time_of_day == 'Morning' and degrees >= 25:
    outfit = 'T-Shirt'
    shoes = 'Sandals'

elif time_of_day == 'Afternoon' and 10 <= degrees <= 18:
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif time_of_day == 'Afternoon' and 18 < degrees <= 24:
    outfit = 'T-Shirt'
    shoes = 'Sandals'
elif time_of_day == 'Afternoon' and degrees >= 25:
    outfit = 'Swim Suit'
    shoes = 'Barefoot'

elif time_of_day == 'Evening' and 10 <= degrees <= 18:
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif time_of_day == 'Evening' and 18 < degrees <= 24:
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif time_of_day == 'Evening' and degrees >= 25:
    outfit = 'Shirt'
    shoes = 'Moccasins'

print (f"It\'s {degrees} degrees, get your {outfit} and {shoes}.")