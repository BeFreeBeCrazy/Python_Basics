product = str(input())
city = str(input())
quantity = float(input())


if city == "Sofia" and product == "coffee":
    total_price = quantity * 0.50
elif city == "Sofia" and product == "water":
    total_price = quantity * 0.80
elif city == "Sofia" and product == "beer":
    total_price = quantity * 1.20
elif city == "Sofia" and product == "sweets":
    total_price = quantity * 1.45
elif city == "Sofia" and product == "peanuts":
    total_price = quantity * 1.60
elif city == "Plovdiv" and product == "coffee":
    total_price = quantity * 0.40
elif city == "Plovdiv" and product == "water":
    total_price = quantity * 0.70
elif city == "Plovdiv" and product == "beer":
    total_price = quantity * 1.15
elif city == "Plovdiv" and product == "sweets":
    total_price = quantity * 1.30
elif city == "Plovdiv" and product == "peanuts":
    total_price = quantity * 1.50
elif city == "Varna" and product == "coffee":
    total_price = quantity * 0.45
elif city == "Varna" and product == "water":
    total_price = quantity * 0.70
elif city == "Varna" and product == "beer":
    total_price = quantity * 1.10
elif city == "Varna" and product == "sweets":
    total_price = quantity * 1.35
elif city == "Varna" and product == "peanuts":
    total_price = quantity * 1.55

print(total_price)