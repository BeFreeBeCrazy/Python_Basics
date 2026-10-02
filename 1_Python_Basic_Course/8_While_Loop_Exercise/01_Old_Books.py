book = str(input())

checked = 0

while True:
    new_book = str(input())
    checked += 1
    if new_book == "No More Books":
        checked -= 1
        print("The book you search is not here!")
        print(f"You checked {checked} books.")
        break
    elif new_book == book:
        checked -= 1
        print(f"You checked {checked} books and found it.")
        break

