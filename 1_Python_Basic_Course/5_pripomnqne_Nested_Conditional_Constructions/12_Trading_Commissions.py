city = str(input())
volume_sales = float(input())
commission = 0.0
is_valid = True

if city == "Sofia":
    if 0 <= volume_sales <= 500:
        commission = 0.05
    elif 500 < volume_sales <= 1000:
        commission = 0.07
    elif 1000 < volume_sales <= 10000:
        commission = 0.08
    elif volume_sales > 10000:
        commission = 0.12
    else:
        is_valid = False
elif city == "Varna":
    if 0 <= volume_sales <= 500:
        commission = 0.045
    elif 500 < volume_sales <= 1000:
        commission = 0.075
    elif 1000 < volume_sales <= 10000:
        commission = 0.10
    elif volume_sales > 10000:
        commission = 0.13
    else:
        is_valid = False
elif city == "Plovdiv":
    if 0 <= volume_sales <= 500:
        commission = 0.055
    elif 500 < volume_sales <= 1000:
        commission = 0.08
    elif 1000 < volume_sales <= 10000:
        commission = 0.12
    elif volume_sales > 10000:
        commission = 0.145
    else:
        is_valid = False
else:
    is_valid = False

calculations = commission * volume_sales

if is_valid == True:
    print (f"{calculations:.2f}")
elif is_valid == False:
    print ("error")
