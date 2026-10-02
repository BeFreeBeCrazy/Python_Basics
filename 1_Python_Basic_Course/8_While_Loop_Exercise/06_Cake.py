length = int(input())
width = int(input())

size_cake = length * width

while True:
    piece = input()
    if piece != "STOP":
        piece = int(piece)
        size_cake -= piece
    if size_cake <= 0:
        print(f"No more cake left! You need {-size_cake} pieces more.")
        break
    if piece == "STOP":
        print(f"{size_cake} pieces are left.")
        break