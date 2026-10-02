squaremeters = int(input())

price = 7.61
discount = 0.18

finalprice = squaremeters * price
finaldiscount = finalprice * discount

finalpriceafterdiscount = finalprice - finaldiscount

print(f"The final price is: {finalpriceafterdiscount} lv.")
print(f"The discount is: {finaldiscount} lv.")