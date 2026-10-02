age = float(input())
sex = str(input())
addressing = ""

if age >= 16 and sex == "m":
    addressing = "Mr."
elif age < 16 and sex == "m":
    addressing = "Master"
elif age >= 16 and sex == "f":
    addressing = "Ms."
elif age < 16 and sex == "f":
    addressing = "Miss"

print (addressing)
