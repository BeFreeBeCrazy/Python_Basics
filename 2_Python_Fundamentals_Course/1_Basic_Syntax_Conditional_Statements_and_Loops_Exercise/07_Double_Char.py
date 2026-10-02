string = str(input())

least_string = ""
while string != "End":
    if string == "SoftUni":
        string = str(input())
        continue
    for _ in string:
        aide = _ * 2
        least_string += aide

    print(least_string)
    least_string = ""
    string = str(input())