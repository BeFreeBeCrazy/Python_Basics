floors = int(input())
apartments_per_floor = int(input())

count_floors = 0

for flrs in range(floors, 0, -1):
    for aps in range(apartments_per_floor):
        if flrs % 2 == 0 and flrs != floors:
            print(f"O{flrs}{aps}", end= " ")
        elif flrs == floors:
            print(f"L{flrs}{aps}", end= " ")
        elif flrs % 2 != 0 and flrs != floors:
            print(f"A{flrs}{aps}", end= " ")
    print()
