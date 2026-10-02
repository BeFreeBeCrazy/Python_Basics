points = int(input())

if points <= 100:
    bonus_points = 5
elif points <= 1000:
    bonus_points = points * 0.2
elif points > 1000:
    bonus_points = points * 0.1

total_points = points + bonus_points


if points % 2 == 0:
    bonus_points += 1
    total_points += 1
elif points % 5 == 0:
    bonus_points += 2
    total_points += 2

print(bonus_points)
print(total_points)