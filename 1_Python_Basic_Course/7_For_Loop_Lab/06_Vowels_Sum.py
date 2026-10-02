text = str(input())
sum_vowels = 0

for _ in text:
    if _ == "a":
        sum_vowels += 1
    elif _ == "e":
        sum_vowels += 2
    elif _ == "i":
        sum_vowels += 3
    elif _ == "o":
        sum_vowels += 4
    elif _ == "u":
        sum_vowels += 5

print (sum_vowels)