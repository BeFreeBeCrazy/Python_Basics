actor_name = str(input())
academy_points = float(input())
evaluators = int(input())

points_gathered = 0



for _ in range(evaluators):
    name_evaluator = str(input())
    given_points = float(input())
    length_names = 0
    length_names += len(name_evaluator)
    calculations = length_names * given_points / 2
    points_gathered += calculations
    totalka = points_gathered + academy_points
    if totalka > 1250.5:
        break

if totalka > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {totalka:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - totalka:.1f} more!")
    