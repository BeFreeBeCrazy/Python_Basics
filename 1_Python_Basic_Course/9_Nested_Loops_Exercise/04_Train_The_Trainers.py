judges = input()
presentation_name = str(input())
presentations = 0

all_marks = 0


while presentation_name != "Finish":
    judges = int(judges)
    presentation_name = str(presentation_name)
    all_grades = 0
    presentations += 1
    for grades in range(judges):
        mark = input()
        all_grades += float(mark)
        all_marks += float(mark)
    print(f"{presentation_name} - {all_grades / judges:.2f}.")
    sum_all_grades = all_marks / judges / presentations

    presentation_name = input()
print(f"Student's final assessment is {sum_all_grades:.2f}.")
