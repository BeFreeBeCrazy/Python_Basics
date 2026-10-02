from math import pi
figure = str(input())


if figure == "square":
    size = float(input())
    print (f"{(size * size):.3f}")
elif figure == "rectangle":
    size = float(input())
    size2 = float(input())
    print(f"{size * size2:.3f}")
elif figure == "circle":
    size = float(input())
    print(f"{pi * (size * size):.3f}")
elif figure == "triangle":
    size = float(input())
    size2 = float(input())
    print(f"{(size * size2) / 2:.3f}")