days = int(input())
food = float(input())

biscuits = 0

dog_food_total = 0
cat_food_total = 0

for x in range(1, days + 1):
    dog_eaten = int(input())
    cat_eaten = int(input())
    if x % 3 == 0:
        biscuits = biscuits + ((dog_eaten + cat_eaten) * 0.1)
    dog_food_total += dog_eaten
    cat_food_total += cat_eaten

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{((dog_food_total + cat_food_total) / food) * 100:.2f}% of the food has been eaten.")
print(f"{dog_food_total / (dog_food_total + cat_food_total) * 100:.2f}% eaten from the dog.")
print(f"{cat_food_total / (dog_food_total + cat_food_total) * 100:.2f}% eaten from the cat.")