steps_needed = 10_000

totalka_steps = 0

while True:
    steps = input()
    if steps != "Going home":
        steps = int(steps)
        totalka_steps += steps
    if totalka_steps >= steps_needed:
        diff = totalka_steps - steps_needed
        print("Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
        break
    if steps == "Going home":
        walking_home = int(input())
        totalka_steps += walking_home
        if totalka_steps >= steps_needed:
            diff = totalka_steps - steps_needed
            print("Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
        else:
            diff2 = steps_needed - totalka_steps
            print(f"{diff2} more steps to reach goal.")
        break