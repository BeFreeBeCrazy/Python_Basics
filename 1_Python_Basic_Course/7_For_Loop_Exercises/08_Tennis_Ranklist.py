tournaments = int(input())
starting_points = int(input())

points_gathered = 0
won_tournaments = 0

for _ in range(tournaments):
    stage = str(input())
    if stage == "W":
        points_gathered += 2000
        won_tournaments += 1
    elif stage == "F":
        points_gathered += 1200
    elif stage == "SF":
        points_gathered += 720

totalka_points = starting_points + points_gathered

print(f"Final points: {totalka_points}")
print(f"Average points: {points_gathered // tournaments}")
print(f"{won_tournaments / tournaments * 100:.2f}%")