movie_type = str(input())
rows = float(input())
columns = float(input())
price = 0.0


if movie_type == "Premiere":
    price = 12
elif movie_type == "Normal":
    price = 7.50
elif movie_type == "Discount":
    price = 5

total_income = rows * columns * price

print(f"{total_income:.2f}")