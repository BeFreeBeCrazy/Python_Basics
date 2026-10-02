width = int(input())
length = int(input())
height = int(input())

apartment_size = width * length * height

while True:
    cardboard = input()
    if cardboard != "Done":
        cardboard = int(cardboard)
        apartment_size -= cardboard
    if apartment_size < 0:
        print(f"No more free space! You need {-apartment_size} Cubic meters more.")
        break
    if cardboard == "Done":
        print(f"{apartment_size} Cubic meters left.")
        break