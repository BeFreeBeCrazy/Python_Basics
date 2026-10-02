not_cool_grades = int(input())

sum_not_cool_grades = 0
count_exercises = 0
avg_score = 0



while sum_not_cool_grades != not_cool_grades:
    exercise_name = str(input())
    if exercise_name == "Enough":
        print(f"Average score: {avg_score / count_exercises:.2f}")
        print(f"Number of problems: {count_exercises}")
        print(f"Last problem: {var_exercise_name}")
        break
    var_exercise_name = exercise_name
    score = int(input())
    count_exercises += 1
    avg_score += score
    if score <= 4:
        sum_not_cool_grades += 1
if sum_not_cool_grades >= not_cool_grades:
    print(f"You need a break, {sum_not_cool_grades} poor grades.")