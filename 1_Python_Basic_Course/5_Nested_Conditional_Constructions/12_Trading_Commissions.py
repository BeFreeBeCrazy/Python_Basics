city = str(input())
volume = float(input())
commission = -1

if city == "Sofia":
    if 0 <= volume <= 500:
        commission = 0.05
    elif 500 < volume <= 1000:
        commission = 0.07
    elif 1000 < volume <= 10000:
        commission = 0.08
    elif volume > 10000:
        commission = 0.12
elif city == "Varna":
    if 0 <= volume <= 500:
        commission = 0.045
    elif 500 < volume <= 1000:
        commission = 0.075
    elif 1000 < volume <= 10000:
        commission = 0.10
    elif volume > 10000:
        commission = 0.13
elif city == "Plovdiv":
    if 0 <= volume <= 500:
        commission = 0.055
    elif 500 < volume <= 1000:
        commission = 0.08
    elif 1000 < volume <= 10000:
        commission = 0.12
    elif volume > 10000:
        commission = 0.145
elif city != 'Sofia' or city != 'Plovdiv' or city != 'Varna':
    print('error') 
if volume < 0:
    print('error')
com = volume * commission
print(f'{com:.2f}')

# elif (city != "Sofia" 
#       or city != "Varna" 
#       or city != "Plovdiv" 
#       and volume < 0):
#     output = 0
# else:
#     output = 1
# if output == 1:
#     print(f'{volume * commission:.2f}')
# elif output == 0:
#     print("error")