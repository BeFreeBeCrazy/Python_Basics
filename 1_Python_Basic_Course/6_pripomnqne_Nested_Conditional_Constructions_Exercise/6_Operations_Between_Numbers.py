number_1 = int(input())
number_2 = int(input())
operator = str(input())
result = 0
printing =""

if operator == "+":
    result = number_1 + number_2
elif operator == "-":
    result = number_1 - number_2
elif operator == "*":
    result = number_1 * number_2

if result % 2 == 0:
    even_odd = "even"
else:
    even_odd = "odd"

if operator == "+" or operator == "-" or operator == "*":
    printing = (f"{number_1} {operator} {number_2} = {result} - {even_odd}")
elif operator == "/" and number_2 == 0:
    printing = (f"Cannot divide {number_1} by zero")
elif operator == "/" and number_2 != 0:
    result = number_1 / number_2
    printing = (f"{number_1} / {number_2} = {result:.2f}")
elif operator == "%":
    if number_2 == 0:
        printing = (f"Cannot divide {number_1} by zero")
    else:
        result = number_1 % number_2
        printing = (f"{number_1} % {number_2} = {result}")

print(printing)