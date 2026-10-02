name = input()

grade = 1
fails = 0

sum_marks = 0

while grade < 12:
    mark = float(input())
    sum_marks += mark
    if mark < 4:
        fails += 1
        if fails > 1:
            print(f"{name} has been excluded at {grade} grade")
            break
        continue
    if grade == 12:
        print(f"{name} graduated. Average grade: {sum_marks / grade:.2f}")
        break
    grade += 1