speed = float(input())

if speed <= 10:
    print("slow")
if 10 < speed <= 50:
    print("average")
if 50 < speed <= 150:
    print("fast")
if 150 < speed <= 1000:
    print("ultra fast")
if speed > 1000:
    print("extremely fast")

# this one is also working because when using elif it doesn't go to the next lines of code, but when using if it does

# speed = float(input())

# if speed <= 10:
#     print("slow")
# elif speed <= 50:
#     print("average")
# elif speed <= 150:
#     print("fast")
# elif speed <= 1000:
#     print("ultra fast")
# elif speed > 1000:
#     print("extremely fast")