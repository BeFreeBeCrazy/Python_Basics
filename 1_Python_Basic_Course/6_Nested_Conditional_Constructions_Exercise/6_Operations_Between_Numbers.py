number1 = int(input())
number2 = int(input())
operator = str(input())

result = 0.0
even_or_odd = ''


if operator == '+':
    result = number1 + number2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
elif operator == '-':
    result = number1 - number2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    pass
elif operator == '*':
    result = number1 * number2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    pass
elif operator == '/':
    if number2 == 0:
        lol_noob = f"Cannot divide {number1} by zero"
    else:
        result = number1 / number2
elif operator == '%':
    if number2 == 0:
        lol_noob = f"Cannot divide {number1} by zero"
    else:
        result = number1 % number2

if operator == '+' or operator == '-' or operator == '*':
    print(f"{number1} {operator} {number2} = {result} - {even_or_odd}")
elif operator == '/':
    if number2 == 0:
        print(lol_noob)
    else:
        print(f"{number1} / {number2} = {result:.2f}")
elif operator == '%':
    if number2 == 0:
        print(lol_noob)
    else:
        print(f"{number1} % {number2} = {result}")